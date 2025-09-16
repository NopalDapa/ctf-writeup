# nothing
> A subtitution cipher? naah, this is Nothing Cipher (TM)

Author: Hanz


## About the Challenge
This challenge gives a chall.zip. when we extract it, given chall.py. There is a dictionary that maps the numbers 1-255 to whitespace patterns (space + tab). The flags are encoded using whitespace steganography. Each flag section is a pattern of spaces followed by tabs, which corresponds to a value in the sbox.

## How to Solve?

To decrypt:

Split the flag at each tab (\t) to get the sections (each section is a space without a tab).
For each section, count the number of spaces (len(p)), then add 1 to get the key (since the SBox starts at 1).
Collect these keys into a list, convert them to bytes, and then decode them to a UTF-8 string.

replace def decrypt() to this code

```
def decrypt():
    parts = flag.split('\t')
    bytes_list = []
    for p in parts[:-1]:  # last part is empty
        num_spaces = len(p)
        key = num_spaces + 1
        bytes_list.append(key)
    b = bytes(bytes_list)
    print(b.decode('utf-8', errors='replace'))

```

then run it, and

<img width="786" height="533" alt="Screenshot from 2025-09-16 21-33-21" src="https://github.com/user-attachments/assets/6f088137-562a-4124-a158-3e10538db969" />

Boom. we got the flag

## Flag
```
HCS{sbox_is_very_cool__ayaya}
```
