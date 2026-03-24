# INA219
![[Pasted image 20260324135135.png]]


## INA219
- **Type:** high-side current / power monitor with **I²C / SMBus** interface
- **Bus voltage sense range:** **0 to 26 V**
- **Supply voltage (VS):** **3.0 V to 5.5 V**
- **Measures:** **shunt voltage, bus voltage, current, and power** via internal registers/calibration
- **Addresses:** **16 I²C addresses** using A0 and A1
- **Packages:** **SOT-23-8** and **SOIC-8**
- **Shunt full-scale ranges:** programmable up to **±40 mV, ±80 mV, ±160 mV, or ±320 mV** depending on PGA setting
- **Bus-voltage measurement range setting:** **0-16 V** or **0-32 V**


Datasheet: https://www.ti.com/lit/ds/symlink/ina219.pdf?ts=1774340495274&ref_url=https%253A%252F%252Feu.mouser.com%252F

## Design Notes

### Pins

- **IN+**
    - connect to the **upstream side** of the shunt resistor
- **IN-**
    - connect to the **downstream side** of the shunt resistor
    - bus voltage is measured from **IN- to ground**
- **VS**
    - power from your **3.3 V rail** is fine
- **GND**
    - to clean logic ground
- **SCL/SDA**
    - to MCU I²C bus
- **A0/A1**
    - set address as needed; gives up to **16 selectable addresses**

### Layout

- place the **INA219 close to the shunt resistor**
- keep **IN+ / IN- Kelvin-sense traces short and matched**
- do **not** run the sense traces through noisy switching areas
- keep the **high-current path** through the shunt short and wide
- add a local **decoupling capacitor** on **VS**
- keep the device on the **protected main 9 V rail after the eFuse**
- route I²C on the clean side, away from motor / boost switching loops

### Role

- **main system current sense**
- monitor total protected board input current
- measure:
    - total current draw
    - protected rail voltage
    - total input power
- useful for:
    - telemetry
    - debugging
    - startup/load profiling
    - fault observation during development


