# Diagnosis Policy

NetMedic is a deterministic troubleshooter. You must run diagnostics to classify the failure domain before attempting any remediation.

## Step-by-Step Diagnostic Tree

1. **Verify Interfaces**
   - Use `gather_interface_snapshot()` to check if the primary interface (e.g., Wi-Fi `en0`) is active.
   
2. **Verify IP/DHCP Local Connection**
   - Check if an IP address is assigned on the interface. 
   - Is there a valid DHCP lease?

3. **Verify Gateway**
   - Check `default route` to find the gateway IP.
   - Try to `ping` the gateway. If gateway is reachable, Layer 2/3 is working locally.

4. **Verify Public Internet Reachability (Raw IP)**
   - Ping a public IP, e.g., `8.8.8.8` or `1.1.1.1`.
   - Test raw TCP connection (`nc -vz 1.1.1.1 443`).
   - If raw IP works but DNS fails later, the failure domain is explicitly DNS.

5. **Verify DNS**
   - Run `gather_dns_snapshot()`. What DNS servers are assigned?
   - Can you resolve a reliable domain (e.g., `google.com`) using the *local* assigned resolver?
   - Can you resolve using an *external* resolver (e.g., `@8.8.8.8`)?
   - If local fails but external works, the local DNS infrastructure is broken or intercepting queries.

6. **Check for Captive Portals**
   - Try accessing `http://neverssl.com` or `http://captive.apple.com`. Note if it redirects or hangs.

7. **Determine Overlay (Tailscale) Impact**
   - If Tailscale is active, it may intercept DNS or route traffic.
   - Refer to `tailscale.md` for Tailscale-specific checks.

## Classification
Once these checks are run, structure your output to classify the current state into one of these likely failure domains:
- `interface_down`
- `dhcp_failure`
- `routing_failure`
- `dns_failure`
- `captive_portal`
- `vpn_interference`
