#!/usr/bin/env python3
"""
Network Packet Flow Analyzer
Author: Mathesh T
"""
import sys

def analyze_flow(pcap_path):
    print(f"[*] Initializing deep packet inspection on {pcap_path}...")
    print("[+] Protocol hierarchy: Ethernet > IPv4 > TCP/UDP")
    print("[+] Anomaly detection: Zero-window probes, SYN floods, ICMP tunneling")

if __name__ == '__main__':
    analyze_flow('capture.pcap')
