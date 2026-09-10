#!/usr/bin/env python3
from pathlib import Path
import argparse, hashlib

p = argparse.ArgumentParser(description="Read-only Qualcomm DEVINFO inspection helper")
p.add_argument("image")
a = p.parse_args()

data = Path(a.image).read_bytes()
print("size:", len(data))
print("sha256:", hashlib.sha256(data).hexdigest())
magic = data.find(b"ANDROID-BOOT!")
print("ANDROID-BOOT! offset:", hex(magic) if magic >= 0 else "not found")

if len(data) > 0x90:
    print("ABL-layout heuristic only:")
    print("0x0d is_unlocked candidate:", hex(data[0x0d]))
    print("0x0e critical-unlock candidate:", hex(data[0x0e]))
    print("0x0f charger-screen candidate:", hex(data[0x0f]))
    print("0x90 verity-mode candidate:", hex(data[0x90]))
    if data[0x90] in (0,1):
        print("candidate verity:", "logging" if data[0x90] == 0 else "enforcing")

for off in range(0, min(256, len(data)), 16):
    row = data[off:off+16]
    hx = " ".join(f"{x:02x}" for x in row)
    asc = "".join(chr(x) if 32 <= x < 127 else "." for x in row)
    print(f"{off:04x}: {hx:<47}  {asc}")
