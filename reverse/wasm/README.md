# WASM (Weird Assembly)
> Aku buat program yang nyusun bouquet buat orang yang spesial. Tapi pas aku balik ke komputer ku kok programnya malah jadi kaya code assembly aneh ya?
ps. coba kalian bikin bouquet terbaik buat orang yang spesial 💐

Author: requiiem


## About the Challenge
This challenge gives a asembbly file that seems weird namely for_that_spesial_someone

## How to Solve?

This is an assembly code that maps each character (letter, number, symbol) to a flower name (e.g., 'A' → 'Rose'). So here we need the inverse of that dict, for a quick lookup from flower to character. Split by spaces, then replace each flower name with its original character. So, I created the following .py file to reverse it.

```
flower_bouquet = {
    'A': 'Rose ',
    'B': 'Camellia ',
    'C': 'Magnolia ',
    'D': 'Poppy ',
    'E': 'Tulip ',
    'F': 'Chrysanthemum ',
    'G': 'Hyacinth ',
    'H': 'Violet ',
    'I': 'Lavender ',
    'J': 'Heather ',
    'K': 'Petunia ',
    'L': 'Gladiolus ',
    'M': 'Yarrow ',
    'N': 'Wisteria ',
    'O': 'Hibiscus ',
    'P': 'Edelweiss ',
    'Q': 'Iris ',
    'R': 'Anemone ',
    'S': 'Kalmia ',
    'T': 'Zinnia ',
    'U': 'Lotus ',
    'V': 'Oleander ',
    'W': 'Begonia ',
    'X': 'Foxglove ',
    'Y': 'Sunflower ',
    'Z': 'Dahlia ',
    'a': 'Jasmine ',
    'b': 'Freesia ',
    'c': 'Bluebell ',
    'd': 'Aconite ',
    'e': 'Orchid ',
    'f': 'Azalea ',
    'g': 'Carnation ',
    'h': 'Ursinia ',
    'i': 'Gardenia ',
    'j': 'Snowdrop ',
    'k': 'Marigold ',
    'l': 'Nerine ',
    'm': 'Aster ',
    'n': 'Xeranthemum ',
    'o': 'Peony ',
    'p': 'Daisy ',
    'q': 'Buttercup ',
    'r': 'Primula ',
    's': 'Crocus ',
    't': 'Verbena ',
    'u': 'Snapdragon ',
    'v': 'Cosmos ',
    'w': 'Delphinium ',
    'x': 'Fuchsia ',
    'y': 'Primrose ',
    'z': 'Scabiosa ',
    '0': 'Hydrangea ',
    '1': 'Amaranth ',
    '2': 'Clematis ',
    '3': 'Pansy ',
    '4': 'Daffodil ',
    '5': 'Lilac ',
    '6': 'Calla ',
    '7': 'Phlox ',
    '8': 'Geranium ',
    '9': 'Amaryllis ',
    '{': 'Canna ',
    '}': 'Silene ',
    '_': 'Thistle ',
    '+': 'Lotuswort ',
    '\\': 'Anthurium ',
    "'": 'Viola ',
    ' ': 'Ixora ',
    ':': 'Cyclamen ',
}

bouquet_flower = {v: k for k, v in flower_bouquet.items()}

def disassemble_bouquet(arrangement):
    stems = arrangement.split(' ')
    return ''.join(bouquet_flower.get(stem + ' ', '') for stem in stems)

special_bouquet = 'Rose Cyclamen Crocus Daisy Orchid Bluebell Gardenia Jasmine Nerine Cyclamen Freesia Peony Snapdragon Buttercup Snapdragon Orchid Verbena Cyclamen Azalea Peony Primula Cyclamen Jasmine Cyclamen Crocus Daisy Orchid Bluebell Gardenia Jasmine Nerine Cyclamen Crocus Peony Aster Orchid Peony Xeranthemum Orchid Ixora Cyclamen Violet Magnolia Kalmia Canna Bluebell Viola Orchid Crocus Verbena Thistle Nerine Jasmine Thistle Cosmos Gardenia Orchid Thistle Orchid Xeranthemum Thistle Primula Peony Crocus Orchid Silene'

print(disassemble_bouquet(special_bouquet))

```

then now we just run solve.py

<img width="786" height="533" alt="Screenshot from 2025-09-16 15-21-46" src="https://github.com/user-attachments/assets/ab028517-a804-44fa-8b78-8c16c1504bd9" />

Boom. we got the flag

## Flag
```
HCS{c'est_la_vie_en_rose}
```
