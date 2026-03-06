#!/usr/bin/env python3
# Society v1 Interactive Influence Simulator (Matplotlib Sliders)
# Run with: python society_v1_simulator.py

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

labels = ["Freedom of Speech (FoS)", "Corruption (Cor)", "Employment (Emp)", "Law Enforcement (LE)", "Gun Rights (Gun)"]
short  = ["FoS", "Cor", "Emp", "LE", "Gun"]
n = 5

def build_A(a_cor_fos, a_cor_le, a_fos_le, a_le_gun, a_emp_cor):
    A = np.eye(n)
    A[1, 0] = a_cor_fos  # Cor <- FoS
    A[1, 3] = a_cor_le   # Cor <- LE
    A[0, 3] = a_fos_le   # FoS <- LE
    A[3, 4] = a_le_gun   # LE  <- Gun
    A[2, 1] = a_emp_cor  # Emp <- Cor
    return A

def simulate(S0, A, eta, steps):
    S_hist = [S0.copy()]
    S = S0.copy()
    for _ in range(int(steps)):
        S_prime = A @ S
        S = (1 - eta) * S + eta * S_prime
        S = np.clip(S, 0.0, 1.0)
        S_hist.append(S.copy())
    return np.array(S_hist)

# Initial values
S0_vals = np.array([0.7, 0.4, 0.8, 0.6, 0.5])
a_vals  = dict(a_cor_fos=-0.3, a_cor_le=-0.5, a_fos_le=-0.1, a_le_gun=-0.4, a_emp_cor=-0.2)
eta0    = 0.3
steps0  = 25

# Figure layout
fig = plt.figure(figsize=(11, 8))
ax_plot = plt.axes([0.08, 0.55, 0.85, 0.40])  # main plot

# Sliders for S (left column)
S_axes = [plt.axes([0.08, 0.51 - i*0.035, 0.35, 0.02]) for i in range(5)]
S_sliders = [Slider(ax, labels[i], 0.0, 1.0, valinit=S0_vals[i], valstep=0.01) for i, ax in enumerate(S_axes)]

# Sliders for A (middle/right column)
A_axes = [plt.axes([0.53, 0.51 - i*0.035, 0.40, 0.02]) for i in range(5)]
A_sliders = [
    Slider(A_axes[0], "Cor ← FoS", -1.0, 1.0, valinit=a_vals["a_cor_fos"], valstep=0.01),
    Slider(A_axes[1], "Cor ← LE ", -1.0, 1.0, valinit=a_vals["a_cor_le"],  valstep=0.01),
    Slider(A_axes[2], "FoS ← LE ", -1.0, 1.0, valinit=a_vals["a_fos_le"],  valstep=0.01),
    Slider(A_axes[3], "LE  ← Gun", -1.0, 1.0, valinit=a_vals["a_le_gun"],  valstep=0.01),
    Slider(A_axes[4], "Emp ← Cor", -1.0, 1.0, valinit=a_vals["a_emp_cor"], valstep=0.01),
]

# Dynamics sliders (bottom)
eta_ax   = plt.axes([0.08, 0.08, 0.35, 0.03])
steps_ax = plt.axes([0.53, 0.08, 0.35, 0.03])
eta_slider   = Slider(eta_ax, "Blend η", 0.0, 1.0, valinit=eta0, valstep=0.01)
steps_slider = Slider(steps_ax, "Steps", 1, 200, valinit=steps0, valstep=1)

# Run button
run_ax = plt.axes([0.43, 0.02, 0.14, 0.04])
run_button = Button(run_ax, "Run Simulation")

# Plot initial
A_current = build_A(**a_vals)
S_hist = simulate(S0_vals, A_current, eta0, steps0)

ax_plot.set_ylim(0, 1)
ax_plot.set_xlabel("Timestep")
ax_plot.set_ylabel("Value (0–1)")
ax_plot.set_title("Society v1 Dynamics")

for i in range(n):
    ax_plot.plot(np.arange(S_hist.shape[0]), S_hist[:, i], label=short[i])
ax_plot.legend(loc="best")

# Text box for states and A
ax_text = plt.axes([0.08, 0.13, 0.85, 0.15])
ax_text.axis("off")
text_obj = ax_text.text(0.01, 0.95, "", va="top", ha="left", family="monospace")

def update_text(S0, S_final, A):
    import numpy as _np
    txt  = "Initial S: " + _np.array2string(_np.round(S0, 3), precision=3, floatmode='fixed') + "\\n"
    txt += "Final   S: " + _np.array2string(_np.round(S_final, 3), precision=3, floatmode='fixed') + "\\n\\n"
    txt += "A (row receives from column):\\n" + _np.array2string(_np.round(A, 2), precision=2, floatmode='fixed')
    text_obj.set_text(txt)

def run(_event=None):
    S0 = np.array([s.val for s in S_sliders])
    A  = build_A(A_sliders[0].val, A_sliders[1].val, A_sliders[2].val, A_sliders[3].val, A_sliders[4].val)
    eta   = eta_slider.val
    steps = int(steps_slider.val)

    S_hist = simulate(S0, A, eta, steps)

    ax_plot.cla()
    for i in range(n):
        ax_plot.plot(np.arange(S_hist.shape[0]), S_hist[:, i], label=short[i])
    ax_plot.set_ylim(0, 1)
    ax_plot.set_xlabel("Timestep")
    ax_plot.set_ylabel("Value (0–1)")
    ax_plot.set_title("Society v1 Dynamics")
    ax_plot.legend(loc="best")
    fig.canvas.draw_idle()

    update_text(S0, S_hist[-1], A)

run_button.on_clicked(run)
update_text(S0_vals, S_hist[-1], A_current)

plt.show()
