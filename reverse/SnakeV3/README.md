# SnakeV3
> pawang ular
ps, run dengan menggunakan command python -m http.server di directory yang sama dengan file file yang diberikan

Author: requiiem


## About the Challenge
This challenge gives a Snakev3.zip when extracted it produces app.css, app.js, index.html and game.wasm

## How to Solve?

Let's focus on game.wasm. Extract it to see what's going on inside. we use command

```
wasm2wat game.wasm -o game.wat

```

<img width="963" height="710" alt="Screenshot from 2025-09-18 15-05-13" src="https://github.com/user-attachments/assets/48b0b44b-dbc9-4736-82b1-810c0c304cdf" />

If we look closely, there are two relevant areas in the memory file:

encrypted_flag is at memory offset 1072
key is at memory offset 1104
If we read both 23-byte blocks and XOR each byte, the result is the flag

So, we create a Uint8Array view: new Uint8Array(instance.exports.memory.buffer, encPtr, LEN)
Do a byte-by-byte XOR: out[i] = enc[i] ^ key[i]
Terminate at null (0x00) if found, or use all 23 bytes. Then decode to string (utf-8).
i made solve.js like this

```
const fs=require('fs');(async()=>{const b=fs.readFileSync('game.wasm');const {instance}=await WebAssembly.instantiate(b,{});const e=instance.exports;const g=v=>typeof v=='object'&&v&&'value' in v?v.value:v;const p=g(e.encrypted_flag),k=g(e.key);const L=23,mem=new Uint8Array(e.memory.buffer);let out='';for(let i=0;i<L;i++)out+=String.fromCharCode(mem[p+i]^mem[k+i]);console.log(out.replace(/\0.*$/,''))})();

```

<img width="786" height="574" alt="Screenshot from 2025-09-18 15-14-48" src="https://github.com/user-attachments/assets/5da38d83-806d-48f5-a67c-774281492fb0" />


Boom. we got the flag

## Flag
```
HCS{baby_s_first_wasm}
```
