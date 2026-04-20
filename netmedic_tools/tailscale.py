import subprocess


def assess_tailscale_options():
    """Checks the status of Tailscale."""
    try:
        result = subprocess.run(["tailscale", "status"], capture_output=True, text=True, check=True)
        return {"status": "success", "running": True, "output": result.stdout}
    except subprocess.CalledProcessError:
        return {"status": "error", "running": False, "message": "Tailscale is not running or not installed."}


def tailscale_up(exit_node=None, debug=False):
    """Brings Tailscale up, optionally routing through an exit node."""
    cmd = ["tailscale", "up"]
    if exit_node:
        cmd.extend(["--exit-node", exit_node])
    if debug:
        cmd.append("--verbose")
    try:
        subprocess.run(cmd, capture_output=True, text=True, check=True)
        return {"status": "success", "message": f"Tailscale is up. Exit node: {exit_node if exit_node else 'none'}"}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "message": f"Exit code {e.returncode}. Error: {e.stderr or e.stdout}"}

def tailscale_down():
    """Brings Tailscale down."""
    try:
        subprocess.run(["tailscale", "down"], capture_output=True, text=True, check=True)
        return {"status": "success", "message": "Tailscale is down."}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "message": f"Exit code {e.returncode}. Error: {e.stderr or e.stdout}"}

