# Open Questions

## Recovery

- What changed outside the intentionally modified slot-B partitions when stock slot A stopped booting?
- Is the global `ro.boot.veritymode=logging` state causal or only a symptom?

## DEVINFO / VerifiedBoot

- Does CTGEN1 use a Qualcomm ABL `ANDROID-BOOT!` DeviceInfo structure in raw `devinfo`?
- Is the relevant VerifiedBoot state stored in `devinfo`, RPMB, or both?
- Does candidate offset `0x90` represent `verity_mode` on this exact build?

## Bootloader unlock

- Is there a safe way to complete or bypass the broken fastboot unlock confirmation path without proprietary keys?
- Is there a signed recovery/boot path accepted by the locked ABL that could provide read-only partition access?

## EDL

- What exact hardware action forces L1561 into Qualcomm 9008 mode?
- Where is the matching signed Firehose for PK hash `3720a9d9e03543ae4ad244d93d4b56ef588a499106c7d1f931f42704173a3414`?

## Reference data

- Can a working CTGEN1 or stock SUNMI T2s L1561 owner provide read-only small-partition dumps?
- Are there commercial refurbishers using a reproducible non-partner method to convert Epos Now/SUNMI units to generic/custom Android?
