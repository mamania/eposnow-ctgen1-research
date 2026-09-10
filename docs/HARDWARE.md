# Hardware notes

Mainboard inspection confirmed Qualcomm SDM660 and shielded compute/power circuitry.

Visible test pads:

- `RX`
- `TX`
- `BOOT`
- `VREG-L13A`

Interpretation:

- RX/TX: likely UART;
- VREG-L13A: regulator test point;
- BOOT: boot/test-mode candidate, possibly relevant to EDL, not proven.

Do **not** short BOOT to VREG-L13A.

RF shields were removed for inspection; no obvious additional EDL-labelled test pad was found beneath them.

The monitor assembly contains a separate I/O/daughterboard with debug USB, power/volume controls, SIM and memory-card interfaces. The SDM660 main compute board remains in the base/main chassis.
