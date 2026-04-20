import json


def classify_state(state_dict):
    """
    Accepts a dictionary of current network state parameters and
    returns a JSON string of the structured classification.
    """
    # In a real setup, this might use Ollama structured outputs directly
    # For now, it enforces that the LLM sends a structured dict to be verified
    
    schema_keys = [
        "interface", "has_dhcp_lease", "has_default_route", 
        "can_ping_gateway", "can_ping_public_ip", "dns_server", 
        "dns_local_works", "dns_external_works", "https_raw_ip_works",
        "tailscale_installed", "tailscale_running", "exit_node_available",
        "likely_failure_domain"
    ]
    
    validated = {k: state_dict.get(k, None) for k in schema_keys}
    
    # Optional logic: force likely_failure_domain if obvious
    if validated["dns_local_works"] is False and validated["dns_external_works"] is True:
        validated["likely_failure_domain"] = "dns"
        
    return json.dumps(validated, indent=2)
