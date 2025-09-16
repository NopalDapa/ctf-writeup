# Reverse Day 1
> Ketika pertama kali belajar reverse engineering, biasanya challenge bisa di-solved cukup dengan strings. Sayangnya, kali ini strings saja belum bisa untuk mendapatkan flag.

Author: Erzyyyy


## About the Challenge
This challenge gives a chall zip

## How to Solve?

first lets extract it. here we got file elf namely day1. lets dissasemmble that to know what it does using this command

```
objdump -d day1 > test.asm

```
now, we got asm file. when we analyze There's a check() function around 121c that:

Has hardcoded bytes that get XORed with 0x5e

Compares the result with the input flag

And then at 1306: xor -0x69(%rbp),%al - this XORs each byte with 0x5e.

```
121c:       48 b8 16 1d 0d 25 2c    movabs $0x3b283b2c250d1d16,%rax
1223:       3b 28 3b 
1226:       48 ba 2c 2d 3b 01 37    movabs $0x3b012d37013b2d2c,%rdx
122d:       2d 01 3b 
1230:       48 89 45 b0             mov    %rax,-0x50(%rbp)
1234:       48 89 55 b8             mov    %rdx,-0x48(%rbp)
1238:       c7 45 c0 3f 24 27 27    movl   $0x2727243f,-0x40(%rbp)
123f:       66 c7 45 c4 27 27       movw   $0x2727,-0x3c(%rbp)
1245:       c6 45 c6 23             movb   $0x23,-0x3a(%rbp)
1249:       c6 45 97 5e             movb   $0x5e,-0x69(%rbp)
```

so i made solve.py to get the flag using XORs each byte with 0x5e

```
flagg = [0x16, 0x1d, 0x0d, 0x25, 0x2c, 0x3b, 0x28, 0x3b, 0x2c, 0x2d, 0x3b, 0x01, 0x37, 0x2d, 0x01, 0x3b, 0x3f, 0x24, 0x27, 0x27, 0x27, 0x27, 0x23]
flag = ''.join(chr(b ^ 0x5e) for b in flagg)
print('Flag:', flag)

```
lets run it

<img width="786" height="533" alt="Screenshot from 2025-09-16 14-17-28" src="https://github.com/user-attachments/assets/3ade9650-964e-4b81-90fb-40c5cd31f1c2" />

Boom. we got the flag

## Flag
```
HCS{reverse_is_eazyyyy}
```
