# Bootloader / A-B research

## Confirmed lock state

- Bootloader locked.
- Secure boot enabled.
- `ro.oem_unlock_supported=1`.
- `ro.boot.flash.locked=1`.

Initially:

```text
fastboot flashing get_unlock_ability
=> 0
```

After writing a valid FRP PersistentDataBlock with the OEM-unlock byte set:

```text
fastboot flashing get_unlock_ability
=> 1
```

The normal unlock path reaches a confirmation UI but fails with:

```text
FAILED (remote: 'Command not support: the display is not enabled')
```

`fastboot oem help` returns `unknown command`, so undocumented OEM fastboot commands are not currently considered a productive route.

## Slot A findings

- A originally booted stock Epos firmware.
- A was not initially marked unbootable.
- Failed boots decremented its retry counter.
- Only after retry exhaustion did A become `unbootable:yes`.
- `fastboot --set-active=a` reset its retry count to 7.
- A still bootlooped afterward and the retry count decreased again.
- A stock-recovery factory reset did not restore normal boot.

Therefore the slot-unbootable state appears to be a result of repeated failed boots rather than the root cause.

## Verity state change

Before experiments:

```text
ro.boot.veritymode=enforcing
```

Now stock recovery on both A and B reports:

```text
ro.boot.veritymode=logging
ro.boot.verifiedbootstate=green
ro.boot.flash.locked=1
```

This global change is one of the strongest reasons shared persistent/security state is under investigation.
