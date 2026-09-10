# Help Wanted

We are looking for technical information and reference data for the **Epos Now CTGEN1 / SUNMI T2s L1561 (Qualcomm SDM660)** platform.

## Highest-value contributions

### 1. Stock CTGEN1 dump or firmware

A complete Epos Now CTGEN1 firmware package or read-only dump from a working unit.

Most useful partitions:

```text
abl_a
boot_a
vbmeta_a
vendor_a
system_a
devinfo
misc
frp
persist
sunmi
```

### 2. Stock SUNMI T2s L1561 dump or firmware

Preferably from the Qualcomm SDM660 L1561 hardware revision.

### 3. Matching Qualcomm Firehose programmer

Target:

```text
HWID:    0008c0e100000000
PK_HASH: 3720a9d9e03543ae4ad244d93d4b56ef588a499106c7d1f931f42704173a3414
```

Multiple public SDM660 loader collections have already been checked and parsed with bkerler tooling. No match has been found so far.

### 4. DEVINFO reference

A raw 4 KiB `devinfo` dump from a working CTGEN1 or stock SUNMI T2s L1561 would be especially valuable.

The current working hypothesis is an ABL-era Qualcomm `ANDROID-BOOT!` structure, but this has not yet been proven on the exact device.

### 5. Hardware / service information

Useful items include:

- confirmed T2s L1561 EDL test point;
- boardview;
- schematic;
- service manual;
- repair-tool notes;
- known conversion/unlock procedure used by refurbishers or service centres.

## How to contribute

Please open a GitHub issue and include:

- exact device model;
- firmware/build if known;
- file size;
- SHA-256;
- source/provenance;
- whether the device was known-good when the data was obtained.

Please redact personal/account data and device serial numbers unless they are technically required.
