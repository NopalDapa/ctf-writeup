# atadatem
> look there are data that seperated!! you should combine them!

Author: Bim

## About the Challenge
This challenge gives a hcs.png

## How to Solve?

atadatem??? hmm... if read from the back, it says metadata. interesting...
Lets read the metadata as the name of the challenge says, im using exiftool with this coomand
```
exiftool hcs.png
```

<img width="743" height="488" alt="Screenshot from 2025-09-15 23-51-00" src="https://github.com/user-attachments/assets/00dea37f-f565-4524-95b5-818d67a75c00" />

I'm suspicious of the contents of the Comment, Description, and keywords. If we try to combine the three, they form a base64 decode.
```
UUF6NjZDdXEvbW9jLm5pYmV0c2FwLy86c3B0dGg=
```
<img width="1852" height="1010" alt="Screenshot from 2025-09-15 23-56-02" src="https://github.com/user-attachments/assets/367f37af-28cd-4191-9f10-c0af3b9e1a83" />

if we read from backward. it will be ```https://pastebin.com/quC66zAQ```, when i search it contains flag that encoded base64. lets submit again in cyber chef

<img width="1852" height="1010" alt="Screenshot from 2025-09-15 23-56-02" src="https://github.com/user-attachments/assets/3847038d-bdb1-4441-a0c5-01cda49c24e3" />

<img width="1852" height="1010" alt="Screenshot from 2025-09-15 23-54-32" src="https://github.com/user-attachments/assets/391d469b-50b4-458d-9707-341905527b0b" />

Boom. we got the flag

## Flag
```
HCS{metadata_can_be_useful_somewhere_somehow_sometime}
```
