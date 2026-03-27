# KsLSI Circuit

### Killswitch + Latching Strapping Pin Isolation

The **KsLSI** is a small circuit I put together while working with the Waveshare ESP32-C6-Pico.

It solves two annoying problems at once:

* I needed a Killswitch for two modules:
	- the **RESET** pin for the *I2C Mux* (which is an open-drain signal)
	- the **STBY** for the motor drivers (regular TTL signal)
* I wanted to use **strapping pins** without breaking boot
	- mechanically isolate the strapping pins on the MCU during initial boot, then close their circuits after startup so I can use them

Instead of burning extra GPIOs, this let me handle both with a single pin.

---

## What It Does

### Killswitch

This part is straightforward.

The circuit lets me control:

* **RESET** → I2C mux reset mode
* **STBY** → motor drivers standby mode

If something needs to be shut down cleanly, held in a safe state, or if the I2C multiplexer needed to get 'unstuck'.

---

### Strapping Pin Isolation

This is the more interesting piece.

ESP32 strapping pins are read during boot to decide how the chip starts. If you mess with them at the wrong time, things break in weird ways. ***Typically, the rule is to avoid using these pins altogether, but they’re still theoretically usable, and rules are meant to be broken.***

So instead of fighting that, I just step out of the way:

* On boot, the pin is **electrically isolated**
* After boot, the circuit **closes and behaves normally**, like good ole' GPIO

No interference, no guessing, no “why isn’t this flashing anymore” moments. Is it safe? Probably not. Will it work for prototyping? Hell yeah!
---

## Why This Exists

This is a **constraint solution**.

The ESP32-C6-Pico doesn’t give you infinite pins, and I didn’t want to dedicate multiple GPIOs just to handle control and boot quirks.

So this circuit compresses responsibility:

* one pin
* two jobs (technically 2.5 jobs (*two different killswitches which is 1.5 jobs, and the strapping isolation job... therefore, 2.5 jobs*) 
* predictable behavior (to a reasonable degree)
* predicatability and reliability?* let us just say yes and hope the magic smoke stays in

---

## Society V1 Context

This is mostly a **prototype-era tool**.

For Society V1, I’m moving to an STM32-based system where I’ll have more than enough pins to:

* avoid strapping pins entirely
* separate control lines properly

So the KsLSI becomes unnecessary in the final design.

---

## Status

**Prototype only**

It’s not part of the final architecture, but it’s a clean way to get there without fighting the hardware the whole time. I am pretty proud of it so I made an entire README.md for it to pat myself on the back 😎
