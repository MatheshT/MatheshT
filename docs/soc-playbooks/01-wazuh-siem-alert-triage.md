# SOC Standard Operating Procedure (SOP): Wazuh SIEM Alert Triage

**Author:** Mathesh T
**Domain:** Defensive Security Operations & SIEM Telemetry

## 1. Triage Workflow Matrix
1. **Alert Ingestion**: Ingest syslog, auditd, and Windows event logs via Wazuh agents.
2. **Severity Classification**:
   - Level 1-4: Informational / System Audits
   - Level 5-9: Moderate Suspicious Activity (e.g. repeated failed logins)
   - Level 10-15: Critical Incident Trigger (e.g. credential dumping, pass-the-hash)
3. **Investigation & False Positive Filtering**.
4. **Containment & Remediation**.
