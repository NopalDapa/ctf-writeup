# Tuff
> Oh my god! You just haxxed this really TUFFFF shop! Give me your best six seven prank and find how to access the flag!

Author: wintertia


## About the Challenge
This challenge gives a tuff ELF, and we should connect with nc to buy flag. but our balance is not enough

## How to Solve?

We initially tried a few common techniques for shop problem:

- Trying integer overflow to change price/balance

Here, one flag requires 100,000 balance. A single purchase allows us to purchase more than one flag. The program handles the new price by calculating the total price = 100,000 x amount, and storing it in an integer data type. An integer has a maximum value of 2,147,483,647. Therefore, we simply input the amount as 21475 to exceed the capacity of an int. In the two's complement number system:

When exceeding the maximum positive limit, the value will "wrap around" to the largest negative value.
The value after overflow: -2,147,483,648 + 16,353 = -2,147,467,295. The program considers the purchase successful because the balance >= cost (1337 >= -2,147,467,295). In fact, our balance also increases to 2,147,468,633 because - (-x) = +x. so, lets input 21475 here

<img width="786" height="533" alt="Screenshot from 2025-09-16 23-04-28" src="https://github.com/user-attachments/assets/5c3d49fd-5e13-411f-9c2a-667c65cb098e" />

Boom. we got the flag

## Flag
```
HCS{u_r_s0_tufff_pl3453_h4ck_m333_4g41nn_<3_44f35687-4e67-49cf-9206-f5a2a9aff57c}
```
