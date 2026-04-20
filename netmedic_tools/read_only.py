import subprocess


def gather_interface_snapshot(interface="en0"):
    """Gathers status, IP, and MAC address of a specific network interface."""
    try:
        result = subprocess.run(["ifconfig", interface], capture_output=True, text=True, check=True)
        return {"status": "success", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "message": str(e)}


def gather_dns_snapshot():
    """Gathers global DNS configuration from scutil."""
    try:
        result = subprocess.run(["scutil", "--dns"], capture_output=True, text=True, check=True)
        return {"status": "success", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "message": str(e)}


def test_public_connectivity(ip="8.8.8.8"):
    """Pings a known public IP address to test routing and general connectivity."""
    try:
        result = subprocess.run(["ping", "-c", "3", ip], capture_output=True, text=True, check=True)
        return {"status": "success", "reachable": True, "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "reachable": False, "message": str(e)}


def test_resolver_path(domain="google.com", server=None):
    """Uses dig to test DNS resolution against a specific server."""
    cmd = ["dig", "+short", domain]
    if server:
        cmd.insert(1, f"@{server}")
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        if result.stdout.strip():
            return {"status": "success", "resolved": True, "output": result.stdout.strip()}
        return {"status": "success", "resolved": False, "output": "No IP returned"}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "resolved": False, "message": str(e)}
