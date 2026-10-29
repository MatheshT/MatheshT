# Brute-Force & Lateral Movement Defense Playbook

**Author:** Mathesh T

## Windows Event Telemetry Correlated
- `4625`: An account failed to log on
- `4624 (Type 3)`: Successful Network Logon
- `4672`: Special privileges assigned to new logon
- `4768 / 4769`: Kerberos TGT / TGS request (Kerberoasting indicator)
