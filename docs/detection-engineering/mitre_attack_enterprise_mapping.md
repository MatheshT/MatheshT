# MITRE ATT&CK Enterprise Mapping Matrix

| Tactic | Technique ID | Description | Detection Mechanism |
| :--- | :--- | :--- | :--- |
| Reconnaissance | T1595 | Active Scanning | Network IDS Scapy sniffer |
| Credential Access | T1003.001 | LSASS Memory Dump | Wazuh Rule 100201 |
| Lateral Movement | T1021.002 | SMB/Windows Admin Shares | Splunk Event 445 Audit |
| Command & Control | T1071.001 | Web Protocols | MCP Security Copilot |
