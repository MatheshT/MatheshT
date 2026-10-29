# AegisForensic AI: SQLite Low-Level Database Carving

**Author:** Mathesh T
**Project:** AegisForensic AI (PhoneDataRecoveryAI)

## Architecture
- Parsing SQLite B-Tree cell payloads and unallocated space.
- Reading Write-Ahead Log (WAL) journal frames for uncommitted deleted records.
- Automated timestamp normalization for WhatsApp, Telegram, and Android SMS databases.
