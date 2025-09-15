# I Forgot Something
> Abis capture network website gweh, tentunya gada yang aneh lah ya?

Author: Rev


## About the Challenge
This challenge gives a chall.pcap

## How to Solve?

We initially tried a few common techniques:

- Analyze chall.pcap using wireshark

Lets try open this pcap using wireshark. i can see many export object using http. lets save them all

<img width="766" height="561" alt="Screenshot from 2025-09-15 10-58-08" src="https://github.com/user-attachments/assets/9104b8eb-9ebd-4889-aa71-fd1d67fd7a08" />

lets see what file we got. we got read.php here. we can cat it, and we got msg encoded by base 64

<img width="748" height="534" alt="Screenshot from 2025-09-15 11-02-11" src="https://github.com/user-attachments/assets/8af9829d-29fd-49cd-95b7-7b5a6f38a8c1" />

lets decode it with CyberChef

<img width="1850" height="1009" alt="Screenshot from 2025-09-15 11-02-24" src="https://github.com/user-attachments/assets/291344dd-b1c0-43b2-8ed0-05d1f3c00117" />


Boom. we got the flag

## Flag
```
HCS{kalian_langsung_filter_flagnya_atau_perhatiin_apa_attackernya_lakukan_hehe}
```
