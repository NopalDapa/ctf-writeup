# Three Umazing Things 
> To Solve this you need three umazing tools to get the flag. Good Luck!

Author: Rev


## About the Challenge
This challenge gives 3 files image. It seems like the author cut the flag into 3 parts and divided it into these 3 different images.

## How to Solve?

We initially tried a few common techniques:

- Using Aperi Solve web to know some steg that avail
- Another tools steg. maybe stegseek?

Let's submit these 3 image to Aperi Solve. started with sedikahuwak.jpg

<img width="1834" height="1003" alt="Screenshot from 2025-09-15 22-39-17" src="https://github.com/user-attachments/assets/ddebccce-609f-445f-bc6b-d059af8e47e3" />

wow, we got the first flag part ```HCS{tIGA_7ooLs``` that hidden with zsteg
Lets go to the next image. we go on hehe.jpg. lets submit it on AperiSolve

<img width="1834" height="1003" alt="Screenshot from 2025-09-15 22-42-39" src="https://github.com/user-attachments/assets/998bb55d-6cc4-4a44-8c62-fcdd888769d9" />

This image contains the part_3.txt file that hidden with binwalk. Because there was an installation error on my binwalk, so I used binwalk online, im using this website https://www.unroll.ing/ . Let's submit it.

<img width="1834" height="1003" alt="Screenshot from 2025-09-15 22-45-02" src="https://github.com/user-attachments/assets/d8c72bd1-09b6-43fb-be63-8118aded3940" />

Lets extract, unzip, and cat the file

<img width="1766" height="752" alt="Screenshot from 2025-09-15 22-46-24" src="https://github.com/user-attachments/assets/c80b8629-e57f-4912-9378-c64c9024e747" />

wow, we got third part of flag ```_K@N_yaK_a0k@W@OWK}```
Last, we go on second part namely brrr.jpg. Same as before, lets submit on aperisolve

<img width="1795" height="1008" alt="Screenshot from 2025-09-15 22-48-43" src="https://github.com/user-attachments/assets/1da47a8b-c76a-4a50-94c3-46f1bf537bd4" />

hmm... nothing suspicious. Let's try another steg tools. maybe stegseek? here i'm using popular word list namely rockyou.txt

<img width="745" height="490" alt="Screenshot from 2025-09-15 22-57-32" src="https://github.com/user-attachments/assets/1dfb1c0f-1cfb-4051-b751-23c23aaf3604" />

wow we got file originally named part_2.txt that saved on grrrr.jpg.out. lets open it

<img width="743" height="486" alt="Screenshot from 2025-09-15 22-59-32" src="https://github.com/user-attachments/assets/8b55737d-e49a-4475-ac8b-76b9617392c2" />

we got last part ```_9a_t3rlalu_5u$Ah```
Lets combine them all

BOOM, we got the flag

<img width="911" height="901" alt="Screenshot from 2025-09-15 10-34-09" src="https://github.com/user-attachments/assets/bf4df688-9b68-4cc0-89d6-1bab111ca483" />

Boom. we got the flag

## Flag
```
HCS{tIGA_7ooLs_9a_t3rlalu_5u$Ah_K@N_yaK_a0k@W@OWK}
```

## Reference

https://www.aperisolve.com/
https://www.unroll.ing/
https://github.com/RickdeJager/stegseek
