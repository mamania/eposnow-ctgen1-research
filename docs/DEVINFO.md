# DEVINFO research

CTGEN1 has a shared 4 KiB `devinfo` partition and separate `abl_a/b`, so ABL-era Qualcomm DeviceInfo is a serious candidate.

## Working layout hypothesis

```text
0x000-0x00C  "ANDROID-BOOT!"
0x00D        is_unlocked
0x00E        is_unlock_critical
0x00F        charger_screen_enabled
0x010-0x04F  bootloader_version[64]
0x050-0x08F  radio_version[64]
0x090        verity_mode
```

Candidate interpretation:

```text
0 -> logging
1 -> enforcing
```

## Why it matters

The device originally reported `ro.boot.veritymode=enforcing`, but stock recovery on both slots now reports `ro.boot.veritymode=logging`, even though A's principal slot-specific partitions were never intentionally written.

A change in shared VerifiedBoot/device state is therefore a plausible explanation.

## Important uncertainty

This exact layout has **not been proven** on CTGEN1.

Secure Qualcomm devices may store VerifiedBoot state through `QCOM_VERIFIEDBOOT_PROTOCOL` using RPMB or another backend instead of treating the raw `devinfo` partition as the sole source of truth.

Blind replacement of the entire 4 KiB partition is therefore high risk.

## SUNMI clue

A public Qualcomm SUNMI V2 Pro project demonstrates practical use of a Qualcomm-style `ANDROID-BOOT!` devinfo structure for bootloader/security-state modification. That device is a different hardware generation, so it is supporting evidence only, not proof of the CTGEN1 layout.
