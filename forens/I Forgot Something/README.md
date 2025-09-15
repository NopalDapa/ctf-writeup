# I Forgot Something
> I want to retrieve my files but I forgot the password. Can you help me?
  Author: Rev

## About the Challenge
This challenge gives a chall.zip files contain flag.txt. but is needed password

## How to Solve?

We initially tried a few common techniques:

- Bruteforcing the key with the Rockyou wordlist

Lets try bruteforcing using rockyou wordlist with this command

```
fcrackzip -v -D -u -p rockyou.txt chall.zip

```
<img width="746" height="489" alt="Screenshot from 2025-09-15 10-33-18" src="https://github.com/user-attachments/assets/9abd5d4a-28f1-4f63-af5d-b427ebd485d8" />

We got the password here : estrella. lets try using to open the flag.txt

```<img width="911" height="901" alt="Screenshot from 2025-09-15 10-34-09" src="https://github.com/user-attachments/assets/bf4df688-9b68-4cc0-89d6-1bab111ca483" />

Boom. we got the flag

## Flag

HCS{makasih_udah_berhasil_bantuin_aku_buat_dapetin_filenya_ehe}
