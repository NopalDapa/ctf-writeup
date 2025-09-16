# Blind File
> Ohh noooo! what is thisss??? can you help me?!?!

Author: Bim

## About the Challenge
This challenge gives Blind file (dont have type)

## How to Solve?

We initially tried a few common techniques:

- Check detail file using exiftool

Lets try check this file using this coomand

```
exiftool file

```

<img width="742" height="486" alt="Screenshot from 2025-09-16 10-30-50" src="https://github.com/user-attachments/assets/f602e210-0c21-465c-a561-ba4c1467f4e8" />

hmm... this file type is ZIP. just extract it. and we got secret.pdf. lets open it

<img width="1500" height="606" alt="Screenshot from 2025-09-16 10-34-07" src="https://github.com/user-attachments/assets/45fddbf1-f5c5-4d7f-bca6-599ceea01baa" />

Boom. we got the flag

## Flag
```
HCS{file_with_no_extension_still_exist_nowadays_XDD}
```
