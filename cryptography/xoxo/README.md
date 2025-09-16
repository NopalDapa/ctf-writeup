# xoxo
> They tried to keep a secret in the relationship, but their habits gave everything away.

Author: Vaa


## About the Challenge
This challenge gives a file .py

## How to Solve?

The chall.py file is a challenge code that generates ciphertext from a flag using XOR with a random key. We need to decrypt the ciphertext back to the original flag using the key that has been found through brute force. Here, the flag is in the format "HCS{...}" starting with bytes [72, 67, 83, 123] ('H', 'C', 'S', '{'). Then we Brute Force on the 4 Byte Key. Then XOR with the ciphertext: flag_candidate = strxor(c_bytes, key_full). Does flag_candidate start with "HCS{"? If yes, we found the flag. so here, i made solver.py like this

```
from Crypto.Util.strxor import strxor

c_hex = "d61a7019ec6a5351aa2d120cf9065b52ec061211c12d1352c12e1056f5065b0de6365e"
c_bytes = bytes.fromhex(c_hex)

key_bytes = bytes([0x9E, 0x59, 0x23, 0x62])
key_full = key_bytes * 9 
key_full = key_full[:35]

flag = strxor(c_bytes, key_full)
print(flag.decode())

```

run it, and

<img width="786" height="533" alt="Screenshot from 2025-09-16 23-26-17" src="https://github.com/user-attachments/assets/bfa85733-8b67-41e0-90fb-f72e3d8c8cf6" />

Boom. we got the flag

## Flag
```
HCS{r3p34t1ng_x0r_1s_t00_w34k_xoxo}

```
