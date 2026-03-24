# Resistor **50 mΩ** 1W, 1%

![[LVK_series_DSL.webp]]
## LVK24R050FER

- **LVK24** = **2412 package**
- **R050** = **50 mΩ**
- **F** = **1% tolerance**
- 4-terminal Kelvin
- 1.0 W @ 70 °C


Shop: https://www.mouser.com/ProductDetail/Ohmite/LVK24R050FER?qs=o85cWoxxEjGvjwnSs%2FOhrQ%3D%3D
Datasheet: https://www.mouser.com/datasheet/3/132/1/res_lvk.pdf
## Design note style
- place in series between:
    - **eFuse OUT**
    - **main protected 9 V distribution node**
- route:
    - **current terminals** in main power path
    - **sense terminals** directly to INA219 IN+ / IN−
### Notes: 
With a **0.05 Ω** shunt, at **2.1 A**: shunt drop = **0.105 V**
- Power in shunt = **I²R = 2.1² × 0.05 ≈ 0.22 W**