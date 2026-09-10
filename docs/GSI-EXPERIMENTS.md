# GSI experiments

Slot B was used for controlled GSI experiments.

## Tested

- phhusson Android 10 / AOSP 10
- phhusson Android 9 / AOSP 9

Both bootlooped.

Only these partitions were intentionally written:

```text
system_b
vbmeta_b
```

These were not intentionally written:

```text
boot_a
boot_b
system_a
vendor_a
vendor_b
vbmeta_a
```

`boot_b` was never written.

Offline inspection found boot-control/shared-data mechanisms but no evidence that either GSI directly overwrote A-specific `boot/system/vendor/vbmeta` partitions.

Possible indirect state changes remain under investigation, including shared `/data`, boot-control metadata, and persistent VerifiedBoot state.
