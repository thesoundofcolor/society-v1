# Intervention vs State Dynamics

## Motivation

Right now the model treats every slider movement as a **change in state**.

If I move a slider down, it simply means that condition is lower in society.  
If I move it up, that condition is higher.

Example:

Lower **Discrimination** → fewer people are discriminating (or feel discriminated).  
Higher **Discrimination** → more discrimination occurring.

This is simple and (somewhat) easy to reason about. That is why the current system uses it.

However, in the real world **two societies can reach the same state through completely different mechanisms**, and those mechanisms matter.

For example:

A society might have low discrimination because of **state dynamics**:

- people culturally reject discrimination
- education and integration reduce prejudice
- economic conditions reduce group tension
- society shames those who discriminate (social stigma through axiomatic force)
- everyone is the same; e.g., no diversity
- extreme diversity where no group has enough cohesion to dominate another

Or a society might have low discrimination because of direct **intervention dynamics**:

- laws aggressively regulate behavior`
- speech restrictions exist
- institutions actively enforce anti-discrimination policy


Both situations produce **low discrimination**, but the downstream effects may differ.

In the first case, free speech may remain largely unaffected. Discrimination declines because of state dynamics such as education, cultural norms, or economic conditions that reduce intergroup hostility. Individuals still retain roughly the same agency and sense of liberty, and social trust may even increase. In this pathway, the system evolves through organic feedback mechanisms rather than direct constraint.

In the second case, discrimination is reduced through direct intervention. Speech restrictions, enforcement mechanisms, and institutional pressure intentionally limit certain forms of expression. While discrimination decreases, the intervention places direct weight on free speech and personal liberty.

The downstream consequences can propagate widely through the system. Restricting speech may reduce perceived personal agency. Reduced agency can influence mental health variables, which may increase the prevalence of coping behaviors such as substance use or addiction. Both of these influences can affect crime, employment, and social trust. These pressures can cascade into poverty, public health burdens, and even increased death-rates. Increased regulatory enforcement may expand institutional authority, which can feed into authoritarian pressure within the system. Economic penalties and compliance structures may also constrain market freedom.

At the end of all this, we have successfully reduced discrimination. Yet the cascade does not stop there. The ripple effects can propagate through multiple variables, even reaching outcomes such as the death-rate, however small the influence may be.

All from trying to change a single variable.

Just look at the mess we can make.

In both cases discrimination is reduced. However, the **pathway used to achieve that outcome** produces very different cascades of influence across the system. What appears to be the same final state at one node of the network may correspond to very different systemic configurations.

Right now the model **cannot distinguish between these pathways**.

It only knows the resulting state.

This idea exists to capture that distinction.

The core motivation here is **realism**. Complex systems often behave differently depending on the *pathway* taken to reach a particular outcome. Two identical states reached through different methods may carry different biases, tradeoffs, and side effects.

Intent and methods matter in society.

Exploring that difference could make the model significantly more expressive and closer to the way real societies behave. It is Society V1's primary ambition. However, what we want to do, and what we can realistically engineer, are two very different things.

For now we must remain in the realm of possible computation.

If we ever want to model this at full realism we would probably need something more powerful, and expensive; something like, I don't know… a quantum computer?

If anyone happens to know where we can borrow one, please let me know.
---

## Concept

The basic idea is to introduce two different ways that slider changes can be interpreted.

### 1. State Mode (current behavior)

Slider movement simply represents a change in societal state.

Examples:

Lower discrimination = fewer discriminatory behaviors or attitudes.  
Higher crime = crime rates increase.  
Lower poverty = fewer people in poverty.

No implication of deliberate policy or intentional intervention is assumed unless it emerges from the modeled state itself. In other words, the system reflects **conditions changing**, not necessarily decisions being made.

State dynamics may still produce outcomes that resemble policy responses (for example, regulatory pressure emerging from environmental stress), but these arise as downstream effects of system conditions rather than explicit interventions.

This is the current design.

---

### 2. Intervention Mode (future concept)

Slider movement represents **intentional societal intervention**.

In this mode the model interprets input as something like:

> society deliberately decides to act in order to change this variable

Examples:

Lower discrimination = anti-discrimination policies, enforcement, cultural campaigns.  
Lower crime = policing expansion, sentencing changes, surveillance, enforcement.  
Increase education = government investment or structural reform.

The important part is that **the mechanism is now intentional action**, not just organic change.

Because intervention mechanisms can produce **secondary effects**, this may change how influences behave.

Example (I know, I keep using discrimination, but it is one of the most clear examples to illustrate this mechanic's impact):

Reducing discrimination organically = little or no direct effect on free speech.

Reducing discrimination through intervention = speech may be restricted through regulation or enforcement.

The state outcome may be identical, but the **causal pathway is different**.

---

## Possible Implementations

This is purely conceptual for now, but there are several ways it could work.

### Modifier button

Hold a button down while moving a slider. (This is my favorite idea so far)

Normal movement = state change.  
Movement while holding modifier = intervention.

This is like a dynamics clutch. Like holding the shift key to type a capital letter. You can move the slider to get state change, or you can move the slider while holding the Intervention button to get intervention dynamics.

---

### Toggle Mode

A switch that turns intervention interpretation on or off.
[ STATE MODE ] or [ INTERVENTION MODE ]

Similar to a caps-lock mechanism.
In intervention mode all slider changes represent deliberate action using intervention dynamics.

---

### Variable-Level Flags

Some variables might support intervention while others remain state-only.

For example:

Intervention might make sense for:

- Discrimination
- Crime
- Corruption
- Education
- Healthcare
- Welfare
- Law Enforcement

But probably not for things like:

- Birthrate
- Addiction
- Innovation

So intervention may only apply to certain parts of the system and be ignored on some variables that don't benefit or need it.

---

### Separate Influence Weights

Another possibility is allowing variables to have different influence behavior depending on mode.

Example:
Discrimination → Free Speech


State reduction = small effect  
Intervention reduction = larger effect

This would allow the model to capture the idea that **policy-driven changes often have side effects that organic changes do not**.

---

## Risks

This feature introduces a lot of complexity.

That is why it is **not being implemented right now**.

Major concerns include:

### Interpretability

The current model is easy to understand.

Slider = state.

Once intervention is introduced, users need to understand that the **same slider movement can mean two different things**.

That increases cognitive load.

---

### Modeling Complexity

Implementing this would introduce significant modeling complexity. It would likely require:

- **Dual influence behavior**  
  Variables would need to behave differently depending on whether the change originates from natural state dynamics or explicit intervention. This means some influences would require conditional logic rather than a single static weight.

- **Additional rules for causal pathways**  
  The model would need mechanisms to track how a state was reached. Two identical variable values might need to propagate different downstream effects depending on the pathway that produced them.

- **Careful tuning to avoid runaway effects**  
  Conditional influence behavior could amplify instability within the network. Without careful constraints, feedback loops could become exaggerated or difficult to stabilize.

This would make the influence matrix significantly harder to reason about, especially once higher-order influence mechanics are introduced.

In other words, the model would need to know not just **where the system is**, but **how it got there**.

---

### Overfitting the Model

One of the biggest dangers is accidentally encoding **political assumptions** instead of modeling mechanisms.

The goal is not to prove that policy intervention is good or bad.

The goal is simply to represent the fact that **different causal pathways can produce different system responses**.

If this feature is implemented poorly it could distort the model.

---

### Debugging Difficulty

If intervention mode exists, it becomes harder to diagnose why a particular cascade occurred.

Was it caused by:

- the variable value
- the intervention pathway
- upstream influence interactions

That makes testing more complicated.

---

## Why It Is Shelved For Now

The current system needs to stay:

- readable
- debuggable
- conceptually clean

Right now the model works best if sliders represent **state only**.

Once the base influence network is stable and higher-order dynamics are being tuned, it may be worth experimenting with this idea.

For now it remains a **future modeling extension**.

---

## Candidate Variables That Might Benefit From This

Not every variable would need intervention interpretation.

The most likely candidates are variables where **policy or social enforcement commonly drive change**.

Examples:

- Discrimination
- Crime
- Corruption
- Education
- Healthcare Access
- Regulation
- Welfare Systems
- Free Speech
- Authoritarianism

These are areas where societies often deliberately intervene rather than relying on purely organic change.

Other variables such as agriculture or diversity probably do not need this feature. Limiting the number of variables that use intervention dynamics could reduce the implementation complexity.

That said, this does not make the problem simple. Even one variable supporting two dynamic systems would already introduce significant modeling difficulty.

---

## Final Thought

One of the motivations for this idea is realism.

In real societies, **state outcomes alone do not tell the whole story**.

Two systems may reach the same numerical condition, but the methods used to get there can produce very different secondary effects.

Capturing that distinction could allow the model to explore how **intent, policy, and social force shape the trajectory of complex systems**, rather than only measuring their final state.

For now, however, the priority is keeping the system understandable and stable while the core influence network is being built.