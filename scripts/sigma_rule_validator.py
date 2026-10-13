#!/usr/bin/env python3
"""
Sigma Detection Rule Validator
Author: Mathesh T
"""
def validate_sigma_structure(yaml_content):
    required_fields = ['title', 'id', 'status', 'description', 'logsource', 'detection', 'level']
    return all(f in yaml_content for f in required_fields)

if __name__ == '__main__':
    print("[*] Sigma validator ready.")
