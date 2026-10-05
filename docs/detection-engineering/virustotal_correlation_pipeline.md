# MCP Security Copilot: VirusTotal Threat Telemetry Correlation

**Author:** Mathesh T

## Data Pipeline
1. Wazuh alerts generate real-time IOCs (hashes, IPs, domain names).
2. FastMCP server routes IOCs to VirusTotal API v3.
3. Threat intelligence verdict is parsed and returned to LLM analyst agent.
