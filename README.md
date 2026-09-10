# Epos Now CTGEN1 / SUNMI T2s L1561 Research

Community reverse-engineering and recovery research for the **Epos Now Countertop Gen1 (CTGEN1)** based on **SUNMI T2s L1561 / Qualcomm SDM660** hardware.

## Current status

The device is **not hard-bricked**: stock recovery and fastboot are still reachable, but normal Android boot currently loops at the SUNMI logo.

What we know now:

- the bootloader is locked and secure boot is enabled;
- slot B was intentionally modified only at `system_b` and `vbmeta_b`;
- slot A later started bootlooping even though its main slot-specific partitions were never intentionally written;
- a stock-recovery factory reset did not fix slot A;
- before the experiments `ro.boot.veritymode=enforcing` was observed;
- stock recovery on **both A and B now reports `ro.boot.veritymode=logging`** while still reporting `ro.boot.verifiedbootstate=green` and `ro.boot.flash.locked=1`;
- the standard FRP/PersistentDataBlock OEM-unlock byte was successfully changed and `fastboot flashing get_unlock_ability` changed from `0` to `1`;
- the normal fastboot unlock confirmation path is broken/disabled on this device;
- a matching signed SDM660 Firehose programmer has not yet been found.

The leading research area is now **shared VerifiedBoot / DeviceInfo state**, especially the 4 KiB `devinfo` partition and any related persistent or RPMB-backed state.

## Help wanted

If you have worked on **Epos Now CTGEN1**, **SUNMI T2s L1561**, Qualcomm SDM660 POS hardware, SUNMI service firmware, or EDL/Firehose tooling, contributions are very welcome.

The most valuable items right now are:

1. a stock **Epos Now CTGEN1** firmware package or read-only dump;
2. a stock **SUNMI T2s L1561** firmware package or read-only dump;
3. a signed Qualcomm Firehose programmer matching:

```text
HWID:    0008c0e100000000
PK_HASH: 3720a9d9e03543ae4ad244d93d4b56ef588a499106c7d1f931f42704173a3414
```

4. a working-device dump of `devinfo`, `misc`, `frp`, `persist`, `sunmi`, `abl_a`, `boot_a`, `vendor_a` or `vbmeta_a`;
5. confirmed T2s L1561 EDL/test-point information or service documentation.

Please open an issue if you have any of these. Even a small read-only dump or a confirmed technical observation can help.

## Goals

- Recover a CTGEN1 that now bootloops after controlled slot-B experiments.
- Understand its A/B boot-control and shared persistent/security state.
- Document a reproducible path to repurpose these terminals for custom Android/POS use.
- Find a matching signed Firehose, CTGEN1 stock dump, or SUNMI T2s L1561 stock dump.

This repo separates **confirmed facts** from **hypotheses**.

## Device

- Epos Now Countertop Gen1 / `CTGEN1`
- SUNMI T2s L1561
- Qualcomm SDM660, ARM64
- Android 9
- Build: `epOS-3.1.13-BASE7-CTGEN1-20231018.145424`
- Recovery: `EposNow/T2s/T2s`, Android 9 `PKQ1.190414.001`
- Kernel: `4.4.153-perf`
- Fastboot product: `T2s`
- Storage: `SDM EMMC`
- Secure boot: yes
- Bootloader: locked
- `ro.oem_unlock_supported=1`
- `ro.boot.flash.locked=1`

## Most important current observation

Before the experiments:

```text
ro.boot.veritymode=enforcing
```

Stock recovery on **both A and B** now reports:

```text
ro.boot.veritymode=logging
ro.boot.verifiedbootstate=green
ro.boot.flash.locked=1
```

Slot A's `system_a`, `boot_a`, `vendor_a`, and `vbmeta_a` were never intentionally written. This strongly suggests a change in shared/persistent boot-security state or in how the boot chain interprets it.

## What was intentionally modified

Only slot B was used for GSI experiments.

Written:
- `system_b`
- `vbmeta_b`

Never intentionally written:
- `boot_a`
- `boot_b`
- `system_a`
- `vendor_a`
- `vendor_b`
- `vbmeta_a`

`boot_b` was never written.

## Slot A

- A originally booted stock Epos firmware.
- A was not initially marked unbootable.
- Failed boots consumed the retry counter.
- Only after retry exhaustion did `slot-unbootable:a` become `yes`.
- `fastboot --set-active=a` reset retry count to 7.
- A still bootlooped afterward and retry count decreased again.
- A stock-recovery factory reset did not fix the bootloop.

Therefore the `unbootable` flag appears to be a **consequence**, not the original cause.

## Bootloader unlock / FRP

Initially:

```text
fastboot flashing get_unlock_ability
=> 0
```

A valid 512 KiB Android PersistentDataBlock was constructed for `frp` with a valid SHA-256 digest, correct magic, payload length 0, and OEM-unlock byte 1.

After flashing:

```text
fastboot flashing get_unlock_ability
=> 1
```

`fastboot flashing unlock` reaches the confirmation UI but fails with:

```text
FAILED (remote: 'Command not support: the display is not enabled')
```

`fastboot oem help` returns `unknown command`.

## EDL / Sahara

Known T2s L1561 identity:

```text
HWID:    0008c0e100000000
PK_HASH: 3720a9d9e03543ae4ad244d93d4b56ef588a499106c7d1f931f42704173a3414
```

Multiple SDM660 Firehose collections were parsed with bkerler's `fhloaderparse.py`. No matching programmer has been found.

EDL/9008 alone is therefore not yet enough; a programmer accepted by this signing chain remains the blocker.

## Shared partitions of interest

| Partition | Size |
|---|---:|
| `devinfo` | 4 KiB |
| `frp` | 512 KiB |
| `misc` | 1 MiB |
| `sunmi` | 10 MiB |
| `persist` | 32 MiB |

There is no separate `bootctrl` partition in the known GPT.

## DEVINFO working hypothesis

Because this device has `abl_a/b` and `xbl_a/b`, an ABL-era Qualcomm `DeviceInfo` layout is a serious candidate:

```text
0x000-0x00C  magic "ANDROID-BOOT!"
0x00D        is_unlocked
0x00E        is_unlock_critical
0x00F        charger_screen_enabled
0x010-0x04F  bootloader_version[64]
0x050-0x08F  radio_version[64]
0x090        verity_mode
```

Candidate meaning:

```text
verity_mode = 0 -> logging
verity_mode = 1 -> enforcing
```

This is **not yet proven for CTGEN1**. Secure Qualcomm builds may back VerifiedBoot state with RPMB or another backend.

## Hardware

Visible mainboard test pads include:

```text
RX
TX
BOOT
VREG-L13A
```

`RX/TX` are likely UART. `VREG-L13A` is a regulator test point. `BOOT` is a strong boot/test-mode candidate but is **not yet proven** to be the EDL strap.

Do not short `BOOT` to `VREG-L13A`.

## What we need most

1. Epos Now CTGEN1 stock firmware/full dump.
2. SUNMI T2s L1561 stock firmware/full dump.
3. Signed Firehose matching the PK hash above.
4. Read-only dump from an identical working device, especially `devinfo`, `misc`, `frp`, `persist`, `sunmi`, `abl_a`, `boot_a`, `vendor_a`, `vbmeta_a`.
5. Confirmed L1561 EDL test-point information or service documentation.

See [WANTED.md](WANTED.md) and the documents in [`docs/`](docs/).

## Safety

This project is for recovery, interoperability and research on hardware you own or are authorized to service.

Do not blindly flash unrelated SDM660 firmware or overwrite security-sensitive partitions without understanding the consequences.
