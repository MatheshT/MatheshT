# Mirage CTF 2.0 - National 1st Place Championship Writeup

**Author:** Mathesh T (BitBr34kers)
**Event:** Mirage CTF 2.0 - National Level Cyber Championship
**Host:** Amrita Vishwa Vidyapeetham

## Overview
Complete technical walkthrough of the binary exploitation and reverse engineering challenges solved during the national championship.

### 1. Stack Buffer Overflow & ROP Chain
- Target binary: `matrix_core_x86_64`
- Vulnerability: Unchecked `gets()` call in authentication subroutine
- Mitigation bypass: ASLR enabled, NX enabled, No Stack Canary
- Exploit strategy: ROP gadget chaining to leak libc base address via `puts@plt(puts@got)`, calculate libc offset, and invoke `system('/bin/sh')`.

```python
from pwn import *
elf = ELF('./matrix_core')
p = remote('mirage-ctf.amrita.edu', 1337)
p.sendline(payload)
p.interactive()
```
