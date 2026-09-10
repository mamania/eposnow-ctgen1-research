# Known Facts vs Hypotheses

This page exists to keep the project from repeatedly re-testing established observations.

## Known facts

- The target is an Epos Now CTGEN1 based on SUNMI T2s L1561 / Qualcomm SDM660.
- Android 9 build: `epOS-3.1.13-BASE7-CTGEN1-20231018.145424`.
- Bootloader is locked; secure boot is enabled.
- Slot B experiments intentionally wrote `system_b` and `vbmeta_b` only.
- `boot_b` was never intentionally written.
- Slot A originally booted stock firmware.
- Slot A became `unbootable` only after its retry counter was exhausted.
- Resetting A active status restored retry count, but did not restore boot.
- Stock-recovery factory reset did not fix the A bootloop.
- `ro.boot.veritymode` was observed as `enforcing` before experiments.
- Both stock recoveries now report `ro.boot.veritymode=logging`.
- Both recoveries still report `ro.boot.verifiedbootstate=green`.
- `fastboot flashing get_unlock_ability` changed from 0 to 1 after a valid FRP PersistentDataBlock reconstruction.
- Normal bootloader unlock confirmation cannot be completed because the display-confirmation path is disabled/broken.
- No separate `bootctrl` partition has been identified.
- A shared 4 KiB `devinfo` partition exists.
- Known T2s L1561 Sahara identity uses PK hash `3720a9d9e03543ae4ad244d93d4b56ef588a499106c7d1f931f42704173a3414`.
- No matching signed Firehose has yet been found in the public collections checked.

## Hypotheses

- Shared persistent state changed during the GSI/boot-attempt sequence.
- `devinfo` is involved in the global verity-mode change.
- The CTGEN1 uses an ABL-era Qualcomm `ANDROID-BOOT!` DeviceInfo structure.
- Candidate ABL offset `0x90` may represent `verity_mode` on this build.
- VerifiedBoot state may instead, or additionally, be RPMB-backed.
- The visible `BOOT` test pad may be an EDL/forced-boot strap.

## Not proven

- That `devinfo[0x90]` is the actual CTGEN1 verity field.
- That writing an external SDM660 `devinfo` sample is safe.
- That `BOOT` shorted to ground enters EDL on this exact board.
- That the GSI directly modified any A-side partition.
- That the global `logging` state alone is the reason stock Android no longer boots.
