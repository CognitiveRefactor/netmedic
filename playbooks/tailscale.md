# Tailscale Policy

If Tailscale is installed on this system, we can use it both to debug and to bypass local network issues.

## Overlay-Aware Logic

1. **Test Overlay Precedence**
   - If `ping 8.8.8.8` works but DNS resolution completely fails, and Tailscale is installed:
     - Check if Tailscale is running.
     - Is MagicDNS intercepting requests?

2. **The Magic Override (Exit Node)**
   - Tailscale Exit Nodes route all traffic (including DNS) through a remote machine via wireguard tunnels (UDP port 41641 usually).
   - If the local network restricts TCP 53/UDP 53 (DNS) but allows arbitrary UDP connections out, bringing up a Tailscale Exit Node bypasses the local broken infrastructure entirely.

### Procedure for the Tailscale Bypass
*Condition:* Public raw IP connectivity works, but DNS/HTTPS fails.
1. Check `tailscale status`.
2. Ask the user if they want to override the local broken network using their preferred Tailscale Exit Node.
3. Execute `tailscale up --exit-node=<preferred_node>`.
4. Re-verify DNS and connectivity.
5. If successful, classify outcome as “overlay workaround successful; local resolver path likely broken”.
