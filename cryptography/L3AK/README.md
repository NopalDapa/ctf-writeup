# Leak
> what is what?

Author: etern1ty


## About the Challenge
This challenge gives a output.txt and chall.py

## How to Solve?

what is what? i think thats clue. Here the code creates an RSA, stores d mod (p-1) (called what) and then writes n, ct, what to a file. Leaking what is what makes the system breakable — from there we can find p, then q, then the private key, then decrypt ct → get the flag. so i made solve.py like this to get the flag


```
from Crypto.Util.number import long_to_bytes, inverse, GCD
import random

n = 132424945097525850654214822436841749617596013766516589461846053019923921509419349878188173267137393388564369574894943951802964034938666342594121858359017467945336230806773103437033058400722533249173019431218833060574032187854004778243330232248639993250668984287478087484530899867973181768171106834615858816947
ct = 8690256152525015206584791844752543379719744787620368046544606811870676380837374553817755653019413372016870108768104936568432345008226950086769230094097164464486596908050930851678115904352532562944170575365724833300330295692157262447360439786705110831106538310141401194897207768598781335529794463310318530218
what = 4701066001566933468539295457165541117336002410834834617743586840140912396231299819496271034686173752299173098904260222360140687146281504574213995930648721
e = 65537

def recover_p(n, e, what, tries=20):
    for _ in range(tries):
        a = random.randrange(2, n-1)
        x = pow(a, e * what, n)
        g = GCD(x - a, n)
        if 1 < g < n:
            return g
    return None

p = recover_p(n, e, what, tries=200)
q = n // p
phi = (p - 1) * (q - 1)
d = inverse(e, phi)
m = pow(ct, d, n)
plain = long_to_bytes(m)
print("Plaintext:", plain)

```

<img width="786" height="533" alt="Screenshot from 2025-09-16 21-06-34" src="https://github.com/user-attachments/assets/f0aa48b0-286a-45b6-8609-0115c40c6c80" />


Boom. we got the flag

## Flag
```
HCS{leak_l3ak_l34k_i_hate_leaks_65746572}
```
