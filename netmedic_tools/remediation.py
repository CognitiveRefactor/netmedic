import subprocess

def flush_dns_cache():
    """Flushes the macOS mDNSResponder local DNS cache (requires sudo)."""
    try:
        result = subprocess.run(["sudo", "killall", "-HUP", "mDNSResponder"], capture_output=True, text=True, check=True)
        return {"status": "success", "message": "DNS cache flushed."}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "message": f"Failed to flush DNS cache: {str(e)}"}

def renew_dhcp(interface="en0"):
    """Renews the DHCP lease for a specific interface."""
    try:
        result = subprocess.run(["sudo", "ipconfig", "set", interface, "DHCP"], capture_output=True, text=True, check=True)
        return {"status": "success", "message": f"DHCP renewed on {interface}."}
    except subprocess.CalledProcessError as e:
         return {"status": "error", "message": f"Failed to renew DHCP: {str(e)}"}
         
def toggle_wifi(interface="Wi-Fi"):
    """Turns Wi-Fi off and then back on."""
    try:
        subprocess.run(["networksetup", "-setairportpower", interface, "off"], check=True)
        subprocess.run(["networksetup", "-setairportpower", interface, "on"], check=True)
        return {"status": "success", "message": "Wi-Fi toggled successfully."}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "message": str(e)}
