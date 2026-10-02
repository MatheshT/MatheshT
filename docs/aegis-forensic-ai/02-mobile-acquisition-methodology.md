# Android Physical & Logical Acquisition Pipeline

**Author:** Mathesh T

## Methodology
- ADB Shell root bridge communication.
- `dd` bit-stream raw block device dump (`/dev/block/bootdevice/by-name/userdata`).
- Live SHA-256 hash stream calculation to establish legal chain of custody.
