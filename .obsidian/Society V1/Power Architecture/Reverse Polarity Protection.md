# P-Channel MOSFET: STD26P3LLH6
![[std26p3llh6.webp]]

## Specs
***Vds:** 30V
**Rds:** 0.03 Ω
**Id:** 12A
**Ptot:** 40W
**Vgs:** ±20
**Package:** DPAK SMD

Datasheet: https://www.st.com/resource/en/datasheet/std26p3llh6.pdf
## Design Notes:
- **Source** 
	- barrel jack / TVS side
- **Drain** 
	- eFuse input side
- **Gate** 
	- **100 Ω** series gate resistor
	- pull-down resistor
		- **100 kΩ** gate pulldown
- **12 V zener**  gate-to-source (optional)


