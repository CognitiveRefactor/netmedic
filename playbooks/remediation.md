# Remediation Policy

Do not execute remediation until you have diagnosed a clear failure domain and consulted the safety policy.

## The Repair Ladder

Run these in order based on the failure domain:

### For Interface / DHCP Failures
1. **Toggle Wi-Fi Interface:** Turn Wi-Fi off and on.
2. **Renew DHCP Lease:** Request a new lease from the router.

### For DNS Failures
1. **Restore Automatic DNS:** Ensure the network settings are configured to receive DNS automatically.
2. **Flush DNS Cache:** Clear the local DNS cache to discard bad records.
3. **Renew DHCP:** (Sometimes necessary to pull correct DNS config).
4. **Tailscale Workarounds:** If local DNS is hopelessly broken, refer to `tailscale.md` for exit node usage.

### For Captive Portals
- Advise the user to open a browser and visit `http://captive.apple.com`.
- We do not currently attempt to automatically bypass or authenticate against captive portals.

### Rollback Expectation
If you change a setting (e.g., set DNS to automatic) and it does not fix the issue, you must evaluate if you should revert that setting before proceeding.
