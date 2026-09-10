# FRP / PersistentDataBlock research

The shared `frp` partition is 512 KiB.

A full-size Android PersistentDataBlock image was constructed with:

- correct SHA-256 digest;
- correct PersistentDataBlock magic;
- payload length = 0;
- OEM-unlock byte = 1 at the last byte of the partition.

After flashing it:

```text
fastboot flashing get_unlock_ability
```

changed from `0` to `1`.

A raw FRP image from an older SUNMI V2 device was also inspected. It used the same standard Android PersistentDataBlock layout: valid digest, the same magic, payload length 0, and the OEM-unlock byte at the end.

That comparison reduces, but does not eliminate, concern that the reconstructed CTGEN1 FRP image had an invalid basic format.
