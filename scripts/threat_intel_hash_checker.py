#!/usr/bin/env python3
"""
Automated Hash Reputation & VirusTotal Telemetry Checker
Author: Mathesh T
"""
import hashlib

def calculate_sha256(filepath):
    h = hashlib.sha256()
    with open(filepath, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            h.update(chunk)
    return h.hexdigest()

if __name__ == '__main__':
    print("[*] Ready to query threat intelligence feeds for IOC hashes.")
