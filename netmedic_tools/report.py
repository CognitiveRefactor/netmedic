def generate_session_report(state_dict, attempted_fixes, resolved=False):
    """
    Generates a Markdown report of the session.
    """
    report = f"""# NetMedic Troubleshooting Report

## Final Status: {"✅ RESOLVED" if resolved else "❌ UNRESOLVED"}

### Symptoms & State
- Likely Failure Domain: {state_dict.get('likely_failure_domain', 'Unknown')}
- Interface: {state_dict.get('interface', 'Unknown')}
- Public Connectivity: {"Working" if state_dict.get('can_ping_public_ip') else "Failing"}
- DNS Resolution: {"Working" if state_dict.get('dns_local_works') else "Failing"}
- Tailscale Overlay Used: {"Yes" if state_dict.get('tailscale_running') else "No"}

### Attempted Fixes
"""
    if attempted_fixes:
        for fix in attempted_fixes:
            report += f"- {fix}\n"
    else:
        report += "- None\n"

    report += "\n### Recommended Next Steps\n"
    if not resolved:
        report += "- Escalation required to IT or use alternative connection (Hotspot).\n"
    else:
        report += "- Monitor connection stability.\n"

    return report
