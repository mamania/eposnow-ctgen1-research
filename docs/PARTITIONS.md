# Partition layout

Important known sizes:

| Partition | Size |
|---|---:|
| `devinfo` | `0x1000` |
| `frp` | `0x80000` |
| `misc` | `0x100000` |
| `sunmi` | `0xA00000` |
| `persist` | `0x2000000` |
| `rawdump` | `0x8000000` |
| `logdump` | `0x4000000` |
| `abl_a/b` | `0x100000` each |
| `dsp_a/b` | `0x1000000` each |
| `modem_a/b` | `0x6E00000` each |
| `vendor_a/b` | `0x32000000` each |
| `system_a/b` | `0xC0000000` each |
| `boot_a/b` | `0x4000000` each |
| `hyp_a/b` | `0x80000` each |
| `tz_a/b` | `0x400000` each |
| `xbl_a/b` | `0x380000` each |
| `vbmeta_a/b` | `0x10000` each |

No separate `bootctrl` partition was identified. No dynamic `super` layout was observed. No `dtbo_a/b` entries were observed in the available partition listing.
