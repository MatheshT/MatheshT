# Kerberoasting Detection & Service Account Hardening

**Author:** Mathesh T

## Detection Logic
- Monitor Windows Event `4769` where Ticket Encryption Type is `0x17` (RC4-HMAC).
- Correlate with service principal names (SPNs) exhibiting high-frequency ticket requests.
