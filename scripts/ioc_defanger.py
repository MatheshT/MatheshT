#!/usr/bin/env python3
"""
Automated IOC Defanging Utility
Author: Mathesh T
"""
def defang_ioc(text):
    return text.replace('http://', 'hxxp://').replace('https://', 'hxxps://').replace('.', '[.]')

if __name__ == '__main__':
    print("[*] IOC Defanger ready.")
