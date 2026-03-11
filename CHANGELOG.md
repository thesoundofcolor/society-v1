# Society V1 - Change Log
Path-Dependent Influence Weights

## 2026-03-10

### The 42
- **v3.1**
  - Added rhettorical questions section to front page paragraph.
  - Worked on Addiction's edge weights table
  - Careated variable formatting macro; now every variable is formatted with: \var{variable name}
  - Changed title from *"Society V1: The 42"* to *"Society V1, Anatomy of the 42"*
  - Worked on making a matrix edge graph using TikZ library but not actually added yet


## 2026-03-09

### The 42
- **v3.0**
  - Added quotes to the header of each variable page
  - Second page for each variable to show influence pathway table
- **v2.6**
  - Finished *Agriculture* section (page 4)

### Research Repo
- **Addiction**
  - Not really much changed, I spent most of the day reading through and making sure all research was valid.


## 2026-03-08

### Repository
- Renamed directories for better usablility. Use lowercase with underscore seperators; Changed "X Y Zed/" "x_y_zed/"
- Moved research repo to root directory

### Research Repo
- Renamed Ukranian documents to have translated English file names
- Found and deleted a random VPN .exe file in crime/cri_agr/  (whoops!)
  - Still remains a mystery on why it was ther but it did correlate to my research work. So I either accidentally download a VPN installer instead of a research .pdf, perhaps a site installed it behind my back (unlikely), or another user followed behind me and installed it there. It was not intalled in my envioronment, and found no further threat. ~E.L. 
- **Addiction**
  - Add/update notes for addiction influences:
    - Add → Agr
	- Add → Aut
  - Added research sources and files to:
	- Add → Agr
  - Added/updated links to:
    - Add → Agr
	- Add → Aut
  
### Intervention vs State Dynamics
- Idea saved as interventio_vs_state_dynamics.md in ./notes/


## 2026-03-07

### The 42
- **v2.5**
  - Refined opening paragraph for clarity and flow.
  - Simplified explanation of variable influence and slider mechanics.
  - Added illustrative example demonstrating influence propagation (Law Enforcement → Crime → downstream effects).
  - Reordered introductory paragraphs to improve conceptual progression and information flow.
  - Added references to companion documents:
    - *Society V1: Whitepaper*
  - Convinced myself page 1 is actually done, but we will see how long that actually lasts (X_x)


## 2026-03-06

### The 42
- **v2.3.2**
  - Removed redundant section on page 2
  - Revised interpretation framework paragraphs for clarity and flow
  - Introduced path-dependent influence weighting framework explanation
- **v2.3.2**
  - Rearranged page 2 to have path-dependence section after metrics & methods. Moved questions after ontology. Much better flow

### New Engine mechanic
- A possibly new second mechanic (just an idea right now): A second mode where rather than a slider change being a state change, it can also be an intentional change.
  - Two modes: 
    - State Mode (normal mode; this is how Societvy V1 treats all transformations) 
	  - Example: Adjusting discrimination down simply means less people are, want to, or can descriminate. Freedom of Speech is barely effected.
	- Intentional Mode (NEW mode; this is making society intentionally change something, through policy or social forces)
	  - Example: Adjusting discrimination down now means anti-discrimination policies are used as the influence. Freedom of Speech is now directly suppressed!
  - Intional influences would be conditional, maybe if you press a button, like a clutch, any user input would use different weights on the influence edge.
    - Not only isn't this a new layer of complexity but it may be impossible to articulate.
	- It would bring the model closer to real-life, but it also might introduce a level of incohereance that might ruin the mechanics. This is just an idea right now...


## 2026-03-05

### The 42
- **v2.1** 
  -Refineded page 1, first paragraph
  - Added explanation for data challenges section
  - Added CMA reference note and formatted italic text
- **v2.2**  
  - Page 1, first paragraph, focused more on abstractions and less on the broader functional dynamics of Society V1.             
- **v2.3**  
  - Finished front page section and formatting 

### Model
- Updated influence matrix relationships for Addiction

### Repository
- Added documents/ and design/ directories
- Introduced central CHANGELOG.md
- Created and commited git repo "society-v1"
- Change repository visibility to public