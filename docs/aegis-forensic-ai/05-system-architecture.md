# AegisForensic AI: System Architecture Diagram

```
[ Android Device ] <--- USB / ADB Bridge ---> [ FastAPI Ingestion Engine ]
                                                          |
                                                          v
                                               [ Bit-Stream Carver ]
                                                          |
                                   +----------------------+----------------------+
                                   |                                             |
                                   v                                             v
                        [ SQLite WAL Parser ]                         [ AI Super-Resolution ]
                                   |                                             |
                                   +----------------------+----------------------+
                                                          |
                                                          v
                                           [ 3D Holographic Forensics HUD ]
```
