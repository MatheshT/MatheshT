# Cyber Apocalypse CTF: Master File Table ($MFT) Carving

**Author:** Mathesh T

## Methodology
- Parsing `$MFT` records using `analyzeMFT` to detect timestamp timestomping.
- Correlating `$LogFile` and `$UsnJrnl` to identify deleted malicious stagers.
