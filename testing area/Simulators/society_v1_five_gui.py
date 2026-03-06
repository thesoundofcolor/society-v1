#!/usr/bin/env python3
"""
Society V1 - 5-Slider Interactive GUI (edge config + node types)

What this provides
------------------
- 5 manual control sliders (nudges): assign each to any of the 42 names
- 5 configurable interactions (edges): choose src, dst, weight (linear value), and node type
- Built-in special edge: Corruption (src) non-linear negative influence on Public Trust (dst)
- Echo cascade with alpha and echo_count
- Plot: the 5 controlled sliders over time + Stress history
- No drift; only reacts to manual nudges

Usage
-----
- Run in PyCharm. Requires numpy and matplotlib.
- Pick which 5 sliders you want to control in the top row (dropdowns).
- On the right, define 5 edges: src, dst, weight, node type (linear/sigmoid/threshold/softclip/power/piecewise/relu).
- The preloaded edge: Corruption -> Public Trust (softclip, negative) is Edge #1 by default.
- Set nudge amounts and click "Apply Nudge(s)".
- Use "Reset to Baseline" to return to the stored baseline.
"""
import numpy as np
import tkinter as tk
from tkinter import ttk
from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# ------------------------- Slider Names (0..41) -------------------------
SLIDER_NAMES: List[str] = [
    "Agriculture","Animals","Birthrate","Corruption","Crime","Deathrate","Diversity",
    "Education Cost","Education Quality","Employment Rate","Energy Production","Equality",
    "Family","Freedom of Speech","Gun Rights","Healthcare Access","Healthcare Cost",
    "Healthcare Quality","Homelesness","Immigration","Infrastructure","Innovation",
    "Police Force","Law Enforcment Budget","Liberty","Capitalism","Mental Health",
    "Military Budget","Minimum Wage","Pollution","Public Trust","Purpose/Meaning",
    "Cost of Living","Racism","Religion","Sickness","Taxes","Socialism","LGB","TQIA+",
    "Technology","Transportation"
]

# ------------------------- Node Function Registry -------------------------
def f_linear(x: float, src: float, dst: float, p: Dict[str, Any]) -> float:
    return float(p.get("gain", 1.0)) * x

def f_sigmoid(x: float, src: float, dst: float, p: Dict[str, Any]) -> float:
    k = float(p.get("k", 6.0)); mu = float(p.get("mu", 0.0))
    scale = float(p.get("scale", 1.0)); offset = float(p.get("offset", 0.5))
    y = 1.0 / (1.0 + np.exp(-k * (x - mu)))
    return scale * (y - offset)

def f_relu(x: float, src: float, dst: float, p: Dict[str, Any]) -> float:
    return max(0.0, x) * float(p.get("gain", 1.0))

def f_threshold(x: float, src: float, dst: float, p: Dict[str, Any]) -> float:
    theta = float(p.get("theta", 0.05)); gain = float(p.get("gain", 1.0))
    return gain * x if abs(x) >= theta else 0.0

def f_softclip(x: float, src: float, dst: float, p: Dict[str, Any]) -> float:
    k = float(p.get("k", 2.0)); scale = float(p.get("scale", 1.0))
    return scale * np.tanh(k * x)

def f_power(x: float, src: float, dst: float, p: Dict[str, Any]) -> float:
    pw = float(p.get("p", 1.5)); gain = float(p.get("gain", 1.0))
    return np.sign(x) * (abs(x) ** pw) * gain

def f_piecewise(x: float, src: float, dst: float, p: Dict[str, Any]) -> float:
    a = float(p.get("a", 0.0)); m1 = float(p.get("m1", 0.5)); m2 = float(p.get("m2", 1.5))
    return m1 * x if x < a else m2 * x

NODE_FUNCS = {
    "linear": f_linear,
    "sigmoid": f_sigmoid,
    "relu": f_relu,
    "threshold": f_threshold,
    "softclip": f_softclip,
    "power": f_power,
    "piecewise": f_piecewise,
}

# ------------------------- Core Data Structures -------------------------
@dataclass
class Edge:
    dst: int
    src: int
    w: float
    fn: str = "linear"
    params: Dict[str, Any] = field(default_factory=dict)
    enabled: bool = True

    def apply(self, delta_src: float, s_src: float, s_dst: float) -> float:
        if not self.enabled or self.fn not in NODE_FUNCS:
            return 0.0
        x = self.w * delta_src
        return float(NODE_FUNCS[self.fn](x, s_src, s_dst, self.params))

@dataclass
class Engine:
    N: int = 42
    edges: List[Edge] = field(default_factory=list)
    alpha: float = 0.5
    echo_count: int = 4
    clip_min: float = 0.0
    clip_max: float = 1.0

    def propagate(self, state: np.ndarray, delta_manual: np.ndarray) -> np.ndarray:
        total = np.zeros(self.N, dtype=float)
        prev = delta_manual.copy()
        scale = 1.0
        for _ in range(self.echo_count):
            contrib = np.zeros(self.N, dtype=float)
            for e in self.edges:
                dv = prev[e.src]
                if dv != 0.0:
                    contrib[e.dst] += e.apply(dv, state[e.src], state[e.dst])
            total += scale * contrib
            prev = contrib
            scale *= self.alpha
        return np.clip(state + total, self.clip_min, self.clip_max)

def stress(state: np.ndarray, baseline: np.ndarray, weights: Optional[np.ndarray] = None, kappa: float = 5.0) -> float:
    if weights is None: weights = np.ones_like(state)
    dev = state - baseline
    C = float(np.sum(weights * (dev ** 2)))
    return 100.0 * (1.0 - np.exp(-C / kappa))

# ------------------------- GUI -------------------------
class FiveGUI:
    def __init__(self, master):
        self.master = master
        master.title("Society V1 — 5-Slider Node GUI")

        # Model
        self.N = 42
        self.engine = Engine(N=self.N, alpha=0.6, echo_count=4)
        self.baseline = np.full(self.N, 0.5, dtype=float)  # swap with your 2025 vector
        self.state = self.baseline.copy()
        self.history = [self.state.copy()]
        self.stress_hist = [stress(self.state, self.baseline)]
        self.max_hist = 120

        # --- Preload the special non-linear edge: Corruption -> Public Trust ---
        # Corruption index = 3, Public Trust index = 30
        self.engine.edges.append(Edge(dst=30, src=3, w=-0.25, fn="softclip", params={"k": 2.5, "scale": 1.0}))

        # Layout
        left = ttk.Frame(master); left.pack(side=tk.LEFT, fill=tk.Y, padx=8, pady=8)
        right = ttk.Frame(master); right.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=8, pady=8)

        # --- Controls: alpha / echo ---
        ttk.Label(left, text="Echo Decay (alpha)").pack(anchor="w")
        self.alpha_var = tk.DoubleVar(value=self.engine.alpha)
        self.alpha_scale = ttk.Scale(left, from_=0.05, to=0.95, orient="horizontal", length=220,
                                     command=lambda v: self._update_alpha(float(v)))
        self.alpha_scale.set(self.engine.alpha); self.alpha_scale.pack(pady=(0,8))

        ttk.Label(left, text="Echo Count").pack(anchor="w")
        self.echo_var = tk.IntVar(value=self.engine.echo_count)
        self.echo_spin = ttk.Spinbox(left, from_=1, to=8, width=5, textvariable=self.echo_var, command=self._update_echo)
        self.echo_spin.pack(pady=(0,12))

        # --- Pick 5 sliders to control + their nudges ---
        ttk.Label(left, text="Manual Controls (pick 5 sliders)").pack(anchor="w", pady=(6,2))
        self.ctrl_vars = []   # combo for which slider
        self.nudge_scales = []
        options = [f"{i:02d} — {SLIDER_NAMES[i]}" for i in range(self.N)]

        rng = np.random.default_rng(13)
        default_idxs = rng.choice(self.N, size=5, replace=False)
        for k in range(5):
            lf = ttk.LabelFrame(left, text=f"Control {k+1}")
            lf.pack(fill=tk.X, pady=4)

            var = tk.StringVar(value=f"{default_idxs[k]:02d} — {SLIDER_NAMES[default_idxs[k]]}")
            cb = ttk.Combobox(lf, values=options, textvariable=var, state="readonly", width=28)
            cb.pack(fill=tk.X, pady=(2,2))
            self.ctrl_vars.append(var)

            ttk.Label(lf, text="Nudge (-0.30 .. +0.30)").pack(anchor="w")
            sc = ttk.Scale(lf, from_=-0.30, to=0.30, orient="horizontal", length=220)
            sc.set(0.0); sc.pack()
            self.nudge_scales.append(sc)

        btns = ttk.Frame(left); btns.pack(fill=tk.X, pady=8)
        ttk.Button(btns, text="Apply Nudge(s)", command=self.apply_nudges).pack(side=tk.LEFT, padx=(0,6))
        ttk.Button(btns, text="Reset to Baseline", command=self.reset_baseline).pack(side=tk.LEFT)

        # --- Edge Config (5 edges) ---
        edges_frame = ttk.LabelFrame(left, text="Edge Config (5 interactions)")
        edges_frame.pack(fill=tk.X, pady=8)

        self.edge_src = []; self.edge_dst = []; self.edge_w = []; self.edge_fn = []
        fn_names = list(NODE_FUNCS.keys())

        # Edge #1: preset Corruption -> Public Trust (softclip, negative)
        for e_idx in range(5):
            row = ttk.Frame(edges_frame); row.pack(fill=tk.X, pady=3)
            ttk.Label(row, text=f"Edge {e_idx+1}").pack(side=tk.LEFT, padx=(0,6))

            src_var = tk.StringVar(value="03 — Corruption" if e_idx==0 else f"{default_idxs[e_idx]:02d} — {SLIDER_NAMES[default_idxs[e_idx]]}")
            dst_var = tk.StringVar(value="30 — Public Trust" if e_idx==0 else f"{(default_idxs[(e_idx+1)%5]):02d} — {SLIDER_NAMES[(default_idxs[(e_idx+1)%5])]}")
            w_var = tk.StringVar(value="-0.25" if e_idx==0 else "0.10")
            fn_var = tk.StringVar(value="softclip" if e_idx==0 else "linear")

            src_cb = ttk.Combobox(row, values=options, textvariable=src_var, state="readonly", width=22); src_cb.pack(side=tk.LEFT, padx=2)
            dst_cb = ttk.Combobox(row, values=options, textvariable=dst_var, state="readonly", width=22); dst_cb.pack(side=tk.LEFT, padx=2)
            w_entry = ttk.Entry(row, textvariable=w_var, width=8); w_entry.pack(side=tk.LEFT, padx=2)
            fn_cb = ttk.Combobox(row, values=fn_names, textvariable=fn_var, state="readonly", width=12); fn_cb.pack(side=tk.LEFT, padx=2)

            self.edge_src.append(src_var); self.edge_dst.append(dst_var); self.edge_w.append(w_var); self.edge_fn.append(fn_var)

        # --- Plots ---
        self.fig, (self.ax1, self.ax2) = plt.subplots(2,1, figsize=(8,6))
        self.canvas = FigureCanvasTkAgg(self.fig, master=right)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        self.update_plot()

    # ----------------- Helpers -----------------
    def _update_alpha(self, v: float):
        self.engine.alpha = float(v)

    def _update_echo(self):
        try:
            self.engine.echo_count = max(1, min(8, int(self.echo_var.get())))
        except Exception:
            pass

    def reset_baseline(self):
        self.state = self.baseline.copy()
        self.history = [self.state.copy()]
        self.stress_hist = [stress(self.state, self.baseline)]
        self.update_plot()

    def _idx_from_combo(self, s: str) -> int:
        return int(s.split("—")[0].strip())

    def _sync_edges_from_ui(self):
        # Rebuild engine.edges from UI selections
        edges = []
        # Always include the special edge first (can be edited in UI as well)
        for e_idx in range(5):
            src = self._idx_from_combo(self.edge_src[e_idx].get())
            dst = self._idx_from_combo(self.edge_dst[e_idx].get())
            try:
                w = float(self.edge_w[e_idx].get())
            except ValueError:
                w = 0.0
            fn = self.edge_fn[e_idx].get().strip()
            if fn not in NODE_FUNCS:
                fn = "linear"
            # default params; for now only softclip/sigmoid/threshold have sensible defaults
            params = {}
            if fn == "softclip":
                params = {"k": 2.5, "scale": 1.0}
            elif fn == "sigmoid":
                params = {"k": 6.0, "mu": 0.0, "scale": 1.0, "offset": 0.5}
            elif fn == "threshold":
                params = {"theta": 0.05, "gain": 1.0}
            edges.append(Edge(dst=dst, src=src, w=w, fn=fn, params=params))
        self.engine.edges = edges

    def apply_nudges(self):
        # Build delta from the 5 control sliders
        delta = np.zeros(self.N, dtype=float)
        chosen = []
        for var, sc in zip(self.ctrl_vars, self.nudge_scales):
            idx = self._idx_from_combo(var.get()); chosen.append(idx)
            delta[idx] += float(sc.get())
        # reset scales to 0 for next move
        for sc in self.nudge_scales: sc.set(0.0)

        # Update edges from UI selections
        self._sync_edges_from_ui()

        # Propagate echoes once
        new_state = self.engine.propagate(self.state, delta)

        # Append to history
        self.state = new_state
        self.history.append(self.state.copy())
        self.stress_hist.append(stress(self.state, self.baseline))
        if len(self.history) > self.max_hist:
            self.history = self.history[-self.max_hist:]
            self.stress_hist = self.stress_hist[-self.max_hist:]

        # Update plot with the 5 chosen sliders
        self.update_plot(chosen_indices=chosen)

    def update_plot(self, chosen_indices: Optional[List[int]] = None):
        H = np.array(self.history)
        T = H.shape[0]

        self.ax1.clear()
        if chosen_indices is None:
            # default to first five selected controls
            chosen_indices = [self._idx_from_combo(v.get()) for v in self.ctrl_vars]
        for idx in chosen_indices:
            self.ax1.plot(range(T), H[:, idx], label=f"{idx:02d}: {SLIDER_NAMES[idx]}")
        self.ax1.set_title("Selected Sliders"); self.ax1.set_xlabel("step"); self.ax1.set_ylabel("value")
        self.ax1.grid(True); self.ax1.legend(fontsize=8, loc="best")

        self.ax2.clear()
        self.ax2.plot(range(T), self.stress_hist)
        self.ax2.set_title("Stress over time"); self.ax2.set_xlabel("step"); self.ax2.set_ylabel("Stress (0–100)")
        self.ax2.grid(True)

        self.fig.tight_layout()
        self.canvas.draw_idle()

def main():
    root = tk.Tk()
    FiveGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
