# EDL / Firehose research

## Known T2s L1561 Sahara identity

```text
HWID:    0008c0e100000000
PK_HASH: 3720a9d9e03543ae4ad244d93d4b56ef588a499106c7d1f931f42704173a3414
```

## Collections already checked

Research has included:

- current bkerler/Loaders collection;
- older bkerler loader snapshots;
- independent Firehose repositories;
- multiple SDM660 programmers from Xiaomi, Lenovo/Motorola, Meizu, Meitu, Sonim, Vivo, Oppo and others.

bkerler's `fhloaderparse.py` was used to extract actual signing information rather than trusting filenames alone.

No programmer with the target PK hash has been identified.

## Consequence

EDL/9008 access alone is not sufficient. Without a programmer accepted by the target signing chain, Sahara may identify the device but arbitrary eMMC access remains blocked.

## Hardware note

A visible `BOOT` test pad exists on the mainboard and may be relevant to forced boot/EDL entry. It is **not yet confirmed** as an EDL strap.

A nearby `VREG-L13A` pad is a regulator test point and must not be treated as the other half of a BOOT short.
