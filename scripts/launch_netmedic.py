import sys
import os

# Add parent dir to path so we can import netmedic_tools
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

try:
    from interpreter import interpreter
except ImportError:
    print("Open Interpreter not installed. Please install it with 'pip install open-interpreter'.")
    sys.exit(1)


def main():
    profile_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "profiles", "netmedic.yaml")
    )

    print("====================================")
    print("      💉 NetMedic initialized      ")
    print("====================================")
    print("Using Open Interpreter with Ollama.")

    # Note: Depending on open-interpreter version, the api varies.
    try:
        import yaml

        # Enforce offline mode to disable telemetry
        interpreter.offline = True
        interpreter.disable_telemetry = True

        # Manually load the profile because interpreter.config_file is not universally supported
        with open(profile_path, 'r') as f:
            config = yaml.safe_load(f)

        if 'llm' in config:
            for k, v in config['llm'].items():
                setattr(interpreter.llm, k, v)

        if 'custom_instructions' in config:
            interpreter.custom_instructions = config['custom_instructions']

        # Disable litellm API checking
        interpreter.llm.model = "ollama/llama3.1:8b"
        interpreter.llm.supports_functions = False
        interpreter.llm.supports_vision = False

        if 'safe_mode' in config:
            interpreter.safe_mode = config['safe_mode']

        if 'auto_run' in config:
            interpreter.auto_run = config['auto_run']

        # Ensure dummy key to satisfy LiteLLM
        interpreter.llm.api_key = "dummy"

        print("\nType your network symptoms below, or type 'exit'.")
        print("Note: For each step, a summary will be provided before the execution prompt.")
        interpreter.chat()
    except Exception as e:
        print(f"\nNetMedic Error: {e}")


if __name__ == "__main__":
    main()
