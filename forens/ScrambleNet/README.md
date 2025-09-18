# ScrambleNet
> I heard the a suspicious employee sent important data in the network?? can you help me to get that data?

Author: Bim


## About the Challenge
This challenge gives a network.pcap

## How to Solve?

We initially tried a few common techniques:

- Analyze chall.pcap using wireshark

Lets try open this pcap using wireshark. When I sorted by time, I noticed the client was trying to send a whole PNG, but it was being chopped up and sent every few hexes. This is indicated by the top packet containing PNG and IHDR, and the last packet containing IEND. However, there's a lot of noise here, namely duplicate hexes sent by the user multiple times. Also, an invalid PNG hex is inserted in the middle.

<img width="1850" height="1053" alt="Screenshot from 2025-09-18 13-46-01" src="https://github.com/user-attachments/assets/d3769b05-753c-4b6d-9e14-4035c82c851a" />

<img width="1850" height="1053" alt="Screenshot from 2025-09-18 13-46-15" src="https://github.com/user-attachments/assets/5fd35a7e-3820-47ee-ae5b-cd3b23177e78" />

To reconstruct the image, I created a script that sorts packets by timestamp and then merges them. I also removed identical hex fragments to reduce noise if the same packet is captured multiple times. I also used DFS to avoid re-exploring the (index, skips_left, buffer_length) combination.the final result of my script is as follows

```
#!/usr/bin/env python3

import argparse
import sys
from pathlib import Path

PNG_SIG = "89504E470D0A1A0A"
IEND_TAG = "49454E44"

def extract_full_hex_from_bytes(b: bytes):
    return b.hex().upper()


def dedupe_fragments(frags):
    seen = set()
    out = []
    for f in frags:
        h = f['hex']
        if h not in seen:
            seen.add(h)
            out.append(f)
    return out

def try_find_png_from_sequence(frags, start_idx=0, max_skips=3, max_bytes=10_000_000):
    n = len(frags)
    sys.setrecursionlimit(10000)
    visited = set()
    def dfs(idx, skips_left, used, skipped, buffer_hex):
        if len(buffer_hex) > max_bytes * 2:
            return None
        key = (idx, skips_left, len(buffer_hex))
        if key in visited:
            return None
        visited.add(key)
        pos = buffer_hex.find(PNG_SIG)
        if pos != -1:
            iend_pos = buffer_hex.find(IEND_TAG, pos)
            if iend_pos != -1 and iend_pos + len(IEND_TAG) + 8 <= len(buffer_hex):
                end = iend_pos + len(IEND_TAG) + 8
                b = bytes.fromhex(buffer_hex[pos:end])
                return (b, used.copy(), skipped.copy())
        if idx >= n:
            return None
        f = frags[idx]['hex']
        res = dfs(idx + 1, skips_left, used + [idx], skipped, buffer_hex + f)
        if res:
            return res
        if skips_left > 0:
            res2 = dfs(idx + 1, skips_left - 1, used, skipped + [idx], buffer_hex)
            if res2:
                return res2

        return None

    return dfs(start_idx, max_skips, [], [], "")


def recover_images(frags, max_skips=3, outdir=Path('.')):
    found = []
    used_global = set()
    skipped_global = set()
    idx = 0
    while idx < len(frags):
        if idx in used_global:
            idx += 1
            continue
        res = try_find_png_from_sequence(frags, start_idx=idx, max_skips=max_skips)
        if not res:
            idx += 1
            continue
        b, used_idxs, skipped_idxs = res
        for u in used_idxs:
            used_global.add(u)
        for s in skipped_idxs:
            skipped_global.add(s)

        found.append({'bytes': b, 'used': used_idxs, 'skipped': skipped_idxs})
        if used_idxs:
            idx = max(used_idxs) + 1
        else:
            idx += 1

    out_files = []
    for i, item in enumerate(found, start=1):
        p = outdir / f'image_{i}.png'
        p.write_bytes(item['bytes'])
        out_files.append(p)

    return out_files, used_global, skipped_global, found


def main():
    pcap = Path('network.pcap')
    max_skips = 10
    outdir = Path('.')

    from scapy.all import rdpcap
    pkts = rdpcap(str(pcap))
    frags = []
    for p in pkts:
        ts = float(p.time) if hasattr(p, 'time') else 0.0
        raw = bytes(p['Raw'].load) if p.haslayer('Raw') else bytes(p)
        full = extract_full_hex_from_bytes(raw)
        if full:
            frags.append({'hex': full, 'ts': ts, 'size': len(full)})
    frags.sort(key=lambda x: x['ts'])
    frags = dedupe_fragments(frags)
    out_files, used_global, skipped_global, found = recover_images(frags, max_skips=max_skips, outdir=outdir)

if __name__ == '__main__':
    main()
    

```
lets run it

<img width="786" height="574" alt="Screenshot from 2025-09-18 13-58-56" src="https://github.com/user-attachments/assets/fbcd8f07-fc2f-481c-a7a3-e5e1c18febbc" />


<img width="1011" height="637" alt="Screenshot from 2025-09-18 13-59-19" src="https://github.com/user-attachments/assets/ec52cd17-98c5-4f3b-ab06-6b59843d2e0b" />

Boom. we got the flag

## Flag
```
HCS{i_hope_you_learn_some_network_scripting_not_do_it_manually^^}
```
