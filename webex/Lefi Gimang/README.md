# I Forgot Something
> LeFi is an attack technique in which attackers trick a web application into either running or exposing files on a web server.

Author: anarchistx


## About the Challenge
This challenge gives a website like this

<img width="1850" height="1006" alt="Screenshot from 2025-09-15 20-56-29" src="https://github.com/user-attachments/assets/6ae8506b-f364-4f1e-a527-7f7584146e7b" />

## How to Solve?

We initially tried a few common techniques:

- Open all available page to analyze

when i open tips.txt, there is pro tip: said Searching with full paths might reveal something interesting...

<img width="1850" height="1006" alt="Screenshot from 2025-09-15 20-58-20" src="https://github.com/user-attachments/assets/45f9e9d3-48a9-437b-943b-c0c44451a8ab" />

on link page. i notice name file is placed behind '?query='. lets try Directory Traversal with '?query=../../../../flag.txt'. 

<img width="1850" height="1006" alt="Screenshot from 2025-09-15 21-03-00" src="https://github.com/user-attachments/assets/fcf3e9f0-faff-412e-a9fc-9fa41cb838e3" />

Boom. we got the flag

## Flag
```
HCS{LFI_buT_n0w_y0u_us1n9_tr4v3r5AL_265f1655-8fab-4469-9eda-7bc191f6935a}
```
