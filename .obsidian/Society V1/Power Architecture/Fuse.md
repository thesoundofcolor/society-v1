# eFuse: TPS259240DRCT
![[Pasted image 20260324124407.png]]

## Specs
- **Vin:** 4.5 V to 13.8 V  
- **Abs max Vin:** 20 V  
- **Ron:** 28 mΩ typ  
- **Current Limit:** 1 A to 5 A (adjustable )  
- **Fault Mode:** Latched  
- **Package:** SON-10 / WSON style
- **Programmable UVLO**
- **Fixed 15 V overvoltage clamp**
- **Blocking FET control pin** for reverse current blocking support

Datasheet: https://www.ti.com/lit/ds/symlink/tps25924.pdf?ts=1774343981586&ref_url=https%253A%252F%252Fefind.ru%252F

## Design Notes:
### Pins
- **IN**
    - from RPP MOSFET drain
- **OUT**
    - to main protected 9 V distribution node
	    - Current sense amplifier
		- 9V boost LED driver
		- 5V buck
		- 3.3V buck
- **ILIM**
    - **45.3 kΩ to GND** for ~**2.1 A typ**  
	    - Place resistor close to IC
    - can increase later if needed, if motors/relays/surges trip the line
- **UVLO**
    - resistor divider for **~7.5–8.0 V** turn-on target
	    - Keep divider close to IC!
- **PGOOD**
    - **use** for telemetry
	    - route to MCU or expose to test pad/pin
	- Use in the future for startup sequencing and fault detection
- **BFET**
    - **leave unused for prototype**, external RPP already exists
    - *Leave a pad or routing option if possible*
- **FLT**
    - Fault Output
    - route to MCU or test pad

### **Layout**
- short, wide power traces
- good copper for thermal spreading
- keep programming resistors close and clean
- short, wide path (***CRITICAL***):
	- **RPP drain → eFuse IN**
	- **eFuse OUT → rail distribution**
		  
- dVdt/ startup
	- this IC does support controlled startup and inrush behavior
	- keep good local capacitance (BULK) after eFuse, keep in mind startup current


### Protection Role

- protects system from:
    - overcurrent
    - sustained overvoltage
    - inrush events
- works in conjunction with:
    - TVS (transient clamp)
    - RPP MOSFET (reverse polarity)