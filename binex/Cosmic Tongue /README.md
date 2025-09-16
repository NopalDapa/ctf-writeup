# Cosmic Tongue
> Waiter, waiter! cast a meteor on this person NOW!

Author: adieos


## About the Challenge
This challenge gives a chall.zip

## How to Solve?
Lets exctract it. and we got chall.py and chall ELF like this

```
#include <stdio.h>
#include <string.h>

int main()
{
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);

    char key[11] = "srynottday";
    char message[20];

    printf("Interstellar bounty hunters have scorched all but this land. And they are marching from the horizon.\n");
    printf("Countless warlocks have fought, yet none prevails against Captain Necron.\n");
    printf("All hope now rests upon thy lips, for thou art the Supernova Sorcerer, whose words alone can tear open the very fabric of this reality!\n");
    printf("Cast thy incantation, mighty one: ");
    fflush(stdout);

    gets(message);
    if (strcmp(message, "opensesame") == 0)
    {
        printf("With a thunderous groan, a secret passage of ancient make hath conjured before thou!\n");
        printf("A portal of golden light opens, beckoning the citizens to flee Captain Necron and his void-born scourges.\n");
        printf("Inside, thou hath found a parchment from the legendary King Midas:\n");
        printf("\"The golden treasure you're looking for is deep inside this land's mantle. Unearth it, and you shall receive victory.\"\n");
    }
    else if (strcmp(key, "opensesame") == 0)
    {
        printf("By your word, the very bedrock doth tremble! Thou hast ripped a fissure in this plane of existence!\n");
        printf("The land opens its mouth and swallows each and every hunters but one.\n");
        printf("For Captain Necron, a special fate: the earth itself doth erupt in a geyser of molten power, a tomb prepared for his very soul.\n");
        printf("The infernal geyser spits out remnants of him, with mystic inscriptions written upon its charred bones:\n");
        FILE *file = fopen("flag.txt", "r");
        if (file == NULL)
        {
            printf("Error opening flag.txt\n");
            return;
        }
        char flag[100];
        fgets(flag, sizeof(flag), file);
        printf("%s\n", flag);
        fclose(file);
    }
    else
    {
        printf("Thy mouth of wisdom hath spoken words of cosmic import: %s\n", message);
        printf("Verily, a phrase of such sorcery hath never been uttered!\n");
        printf("Dreaded Captain Necron flees from the scene.. biding his time until thy final hour to return and lay waste to this land!\n");
    }

    return 0;
}

```

I think this challenge about buffer overflow. we should overwrite key[srynottday] into key[opensesame], lets read assembly this code. and we got
```
# Key buffer initialization:
0x000000000000129e <+85>:    mov    %rax,-0x13(%rbp)    # key[0..7]
0x00000000000012a2 <+89>:    movw   $0x7961,-0xb(%rbp)  # key[8..9] 
0x00000000000012a8 <+95>:    movb   $0x0,-0x9(%rbp)     # key[10] = '\0'

# Message buffer access:
0x00000000000012fc <+179>:   lea    -0x30(%rbp),%rax    # message buffer
0x0000000000001308 <+191>:   call   0x1120 <gets@plt>   # gets(message)
```

we can see. there is buffer key and message offset. convert it to decimal 

key offset: -0x13 = -19 decimal
message offset: -0x30 = -48 decimal

from that we can count offset to lead buffer overflow goes to key using

offset = |(-48)-(-19)| = 29

alright. lets input using char A 29 times followed by the text opensesame

<img width="786" height="533" alt="Screenshot from 2025-09-16 11-11-15" src="https://github.com/user-attachments/assets/40405765-8818-4bbb-b5a0-e3118ea080c3" />


Boom. we got the flag

## Flag
```
HCS{y0ur_w15hhh_15_my_c0mm4nd_51r3_ddb9c6d1-b788-4b90-a66e-4c0f0173cd73}
```
