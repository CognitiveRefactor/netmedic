# 💉 NetMedic

NetMedic is an agentic network troubleshooting utility for macOS. It uses a local LLM (via Ollama) and Open Interpreter to diagnose and remediate common network issues using a set of purpose-built diagnostic tools.

## 🚀 How it Works

NetMedic follows a multi-step process to get you back online:
1.  **Diagnosis**: Gathers snapshots of your network interfaces, DNS configuration, and public connectivity.
2.  **Classification**: Analyzes the data to identify the likely failure domain (Interface, DHCP, DNS, or Captive Portal).
3.  **Remediation**: Proposes and executes fixes based on a "Repair Ladder" policy, ranging from flushing DNS caches to setting up Tailscale exit nodes.

## 🛠 Prerequisites

NetMedic is designed specifically for **macOS** and requires the following:

- **Python 3.9+**
- **Ollama**: Running locally with the `llama3.1:8b` model.
- **Open Interpreter**: Used as the execution engine.
- **Sudo Privileges**: Required for certain remediation steps like flushing DNS or renewing DHCP leases.
- **Tailscale (Optional)**: If installed, NetMedic can use it to bypass local network restrictions.

## 📦 Installation

1.  **Install Open Interpreter**:
    ```bash
    pip install open-interpreter
    ```

2.  **Install Ollama**:
    Download it from [ollama.com](https://ollama.com) and pull the required model:
    ```bash
    ollama pull llama3.1:8b
    ```

3.  **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/netmedic.git
    cd netmedic
    ```

## 🏃 Usage

Launch NetMedic using the provided script:

```bash
python3 scripts/launch_netmedic.py
```

Once launched, describe your symptoms (e.g., *"I can ping IP addresses but websites won't load"*) and NetMedic will begin its diagnostic routine.

> [!IMPORTANT]
> NetMedic will ask for your approval before running any remediation commands. Always review the "Summary" provided before typing `y`.

## 📂 Project Structure

- `scripts/`: Contains the main entry point (`launch_netmedic.py`).
- `netmedic_tools/`: Python modules for low-level network interactions (`read_only.py`, `remediation.py`, etc.).
- `profiles/`: Configuration for Open Interpreter and LLM settings.
- `playbooks/`: Markdown-based policies that guide the AI's troubleshooting logic.
- `configs/`: Local environment preferences.

## 🛡 Safety & Policy

NetMedic is governed by strict diagnostic and safety policies defined in the `playbooks/` directory. It is designed to be "read-first," gathering all necessary information before attempting any changes to your system settings.

---
*Disclaimer: NetMedic is a troubleshooting aid. Use it at your own risk. Always ensure you have a backup of critical network configurations.*
