#!/usr/bin/env python3
"""
Wazuh JSON Syslog Event Parser & Alert Triage Utility
Author: Mathesh T
"""
import json

def parse_alert(line):
    try:
        data = json.loads(line)
        rule_id = data.get('rule', {}).get('id')
        level = data.get('rule', {}).get('level')
        return rule_id, level
    except Exception:
        return None, None

if __name__ == '__main__':
    print("[*] Wazuh log parser operational.")
