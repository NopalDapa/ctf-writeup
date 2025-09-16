#   Toggle
> Maw flag

Author: Thehxnz

## About the Challenge
This challenge gives a website and file setup.sol

<img width="1841" height="1016" alt="Screenshot from 2025-09-16 10-38-50" src="https://github.com/user-attachments/assets/403495b5-32b1-4201-8b15-8c40fc2d8ede" />

## How to Solve?

First, Let's follow instruction to using
```
curl -sSfL https://pwn.red/pow | sh -s s.AAAnEA==.b7z/FNg4P/8OkpnDWP6O0A==
```
hmm... we got some weird strings like encode base64, but it doesn't. so i try input this strings to solution bar on website. yeah it correct. now we can launch and get some credentials

<img width="1841" height="1016" alt="Screenshot from 2025-09-16 10-45-49" src="https://github.com/user-attachments/assets/62963cf4-eaa6-4845-9a60-46d15b10023a" />

here, we also given setup.sol to signed contract. so i made file signed.py like this to sign contract

```
from web3 import Web3

RPC_URL = "http://intersec.hcs-team.com:12322/073796d4-0bcb-4164-8787-c4501d018729"
PRIVKEY = "2daba1583837f3d1cb214823be39c1d3b9a8c3d8759af11751c35cf2adfa0b4e"
SETUP_CONTRACT_ADDR = "0xb05101DddE2f118501524b6D510061dA532e0FfE"
WALLET_ADDR = "0x1Df059D98143d72770830333376EA325f6d5F9F4"

abi = [
    {"inputs": [], "name": "solve", "outputs": [], "stateMutability": "nonpayable", "type": "function"},
    {"inputs": [], "name": "isSolved", "outputs": [{"internalType": "bool", "name": "", "type": "bool"}], "stateMutability": "view", "type": "function"}
]

w3 = Web3(Web3.HTTPProvider(RPC_URL))
contract = w3.eth.contract(address=SETUP_CONTRACT_ADDR, abi=abi)

tx = contract.functions.solve().build_transaction({
    'from': WALLET_ADDR,
    'nonce': w3.eth.get_transaction_count(WALLET_ADDR),
    'gas': 100000,
    'gasPrice': w3.eth.gas_price
})

signed_tx = w3.eth.account.sign_transaction(tx, private_key=PRIVKEY)
tx_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)
print("Tx hash:", tx_hash.hex())

receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
print("Solved status:", contract.functions.isSolved().call())
```

Solved status said True. back to the web and get again the flags

<img width="1841" height="1016" alt="Screenshot from 2025-09-16 10-48-37" src="https://github.com/user-attachments/assets/47c7279b-d27e-486d-828c-70ab89404a17" />

Boom. we got the flag

## Flag
```
HCS{minat_belajar_blockchain?_hubungi_mas_hanz}
```
