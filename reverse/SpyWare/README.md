# SpyWare
> Temen ku ngasih kunjaw ETS ATP/Dasprog/(insert nama matkul pengenalan pemrograman di depart kalian) nih, tapi kok ga mau jalan yh?

Author: requiiem


## About the Challenge
This challenge gives a kunci_jawaban.py

## How to Solve?

In this challenge, the author was a bit mischievous. He tried importing os and rm -rf all directories. These are dangerous commands that can wipe out the entire file system. Fortunately, there was an error in the code, so it wasn't executed. Let's be more careful by reading the code first.

<img width="786" height="574" alt="Screenshot from 2025-09-16 15-40-20" src="https://github.com/user-attachments/assets/30077667-1128-429f-b03c-e96ad0d3405a" />

There are several things I did to make this code work.
- remove this line ```import random ;import os; os.system("rm -rf /") import sys```
- change this line ```if flag = "":``` into this ```if flag == "":```
- and remove hidden code section on the right

<img width="1444" height="825" alt="Screenshot from 2025-09-16 15-26-17" src="https://github.com/user-attachments/assets/e1da5b1c-bbfc-425e-9a16-8b9490bb0213" />

After doing that 3 things, lets execute again

<img width="786" height="574" alt="Screenshot from 2025-09-16 15-49-34" src="https://github.com/user-attachments/assets/a3998a06-4e12-4009-8361-b0f2c9e224e6" />


Boom. we got the flag

## Flag
```
HCS{tengs_kunci_jawabannya_brok_semoga_lu_dapet_nilai_A_yee}
```
