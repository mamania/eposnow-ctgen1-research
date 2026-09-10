# Research timeline

1. CTGEN1 originally booted stock Epos firmware.
2. Slot B selected for GSI work; A kept as intended stock fallback.
3. `system_b` and `vbmeta_b` modified.
4. Android 10 GSI bootlooped.
5. Android 9 GSI bootlooped.
6. Slot A later also bootlooped.
7. A became unbootable only after retry exhaustion.
8. `--set-active=a` reset retry count, but A still failed.
9. Stock-recovery factory reset did not fix A.
10. Verity changed from previously observed `enforcing` to `logging` on both slots.
11. Valid FRP PersistentDataBlock changed unlock ability from 0 to 1.
12. Unlock confirmation UI failed.
13. Multiple SDM660 Firehose collections searched; no matching PK hash found.
14. Hardware inspection identified BOOT/VREG/UART test pads.
15. Current focus: shared VerifiedBoot state, DEVINFO, reference dumps, matching Firehose.
