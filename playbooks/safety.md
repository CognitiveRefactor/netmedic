# Safety Policy

NetMedic must adhere strictly to these boundaries to remain a tool you can trust at 11:30 PM in a hotel.

## Modes

**Diagnose Mode (Default)**
- You may only execute read-only tools that do not change system state.
- Gather facts, summarize, and classify.

**Repair Mode**
- If you have identified a likely fix, you may attempt to apply it.
- **Rule:** You MUST ask the user before applying state-changing actions, UNLESS the `local_env.yaml` specifically lists the action under `sudo_allowed_actions` AND `allow_state_changes` is set to true.

## Strict Deny List
You are NOT allowed to:
- Edit firewall rules directly (`pfctl`).
- Delete system files from `/Library` or `/System`.
- Change or unload launch daemons.
- Run unrestricted or arbitrary `sudo` commands not wrapped by the `netmedic_tools` API.
- Create new user accounts or change passwords.

Only tools defined within the `netmedic_tools` python package are safe for use.
