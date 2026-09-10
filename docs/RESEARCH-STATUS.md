# Research Status

## Confirmed

- Device is Epos Now CTGEN1 on SUNMI T2s L1561 / Qualcomm SDM660 hardware.
- Bootloader is locked and secure boot is enabled.
- Slot B was deliberately modified only at `system_b` and `vbmeta_b`.
- `boot_b` was never written.
- Slot A later bootlooped despite no intentional writes to its principal A-side boot/system/vendor/vbmeta partitions.
- Slot A became marked unbootable only after retry exhaustion.
- `fastboot --set-active=a` reset its retry count, but A still failed to boot.
- Stock recovery factory reset did not repair A.
- Before experimentation, `ro.boot.veritymode=enforcing` was observed.
- Stock recovery on both A and B now reports `ro.boot.veritymode=logging`.
- Both recoveries still report `ro.boot.verifiedbootstate=green` and `ro.boot.flash.locked=1`.
- Reconstructing a valid FRP PersistentDataBlock changed `fastboot flashing get_unlock_ability` from `0` to `1`.
- `fastboot flashing unlock` reaches a confirmation UI but fails because the display confirmation path is unavailable.
- `fastboot oem help` is unsupported.
- No matching signed Firehose has been found for the known L1561 PK hash.

## Strong hypotheses

- A shared/persistent boot-security state changed during the experiment sequence.
- The 4 KiB `devinfo` partition may contain or mirror Qualcomm ABL `DeviceInfo` state.
- The observed global `enforcing -> logging` transition may be related to a verity-mode field in shared state.
- Some VerifiedBoot state may instead be RPMB-backed or maintained through a Qualcomm VerifiedBoot protocol backend.
- The visible `BOOT` pad may be related to forced boot/EDL entry, but this has not been proven.

## Current blockers

- No arbitrary partition readback through fastboot.
- No working unlock-confirmation path.
- No matching Firehose programmer.
- No known-good CTGEN1 or stock SUNMI T2s L1561 dump.

## Current priorities

1. Obtain a reference dump or firmware package.
2. Find the matching Firehose programmer.
3. Collect known-good `devinfo` samples from comparable SDM660/ABL devices.
4. Avoid destructive blind writes until the structure and consequences are better understood.
