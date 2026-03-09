import os
import re

# === Root Folder Name ===
root = "Research"

# === Variable Slider List === Enter slider list below
sliders = [
    "Addiction",
    "Agriculture",
    "Authoritarianism",
    "Birthrate",
    "Corruption",
    "Cost of Living",
    "Crime",
    "Deathrate",
    "Discrimination",
    "Diversity",
    "Education Accessibility",
    "Education Cost",
    "Education Quality",
    "Employment",
    "Energy",
    "Equality",
    "Family",
    "Freedom Of Speech",
    "Gun Rights",
    "Healthcare Access",
    "Healthcare Cost",
    "Healthcare Quality",
    "Homelessness",
    "Immigration",
    "Infrastructure",
    "Innovation",
    "Law Enforcement",
    "Liberty",
    "Market Freedom", 
    "Mental Health",
    "Military Budget",
    "Minimum Wage",
    "Pollution",
    "Poverty",
    "Public Trust",
    "Purpose",
    "Religion",
    "Sickness",
    "Taxes",
    "Technology",
    "Transportation",
    "Wellfare"

]
# this is a bit messy, but hey it works. Maybe refine it later? Maybe not, probably too much work (X_x)
# convert slider name to short code, use first three letters, and for duplicates we also append the second word's first letter "edua"= "education access" & "eduq" = "education quality"
def short_code(name):
    words = name.lower().split()
    code = ''.join(re.findall(r"[a-z]", words[0]))[:3]
    # If duplicate base code appears, append first letter of second word
    if len(words) > 1:
        code += words[1][0]
    return code

# Create root folder
os.makedirs(root, exist_ok=True)

# Generate code dictionary
codes = {name: short_code(name) for name in sliders}

# Build the nested folder structure
for influencer in sliders:
    influencer_folder = os.path.join(root, influencer)
    os.makedirs(influencer_folder, exist_ok=True)
    inf_code = codes[influencer]

    for influenced in sliders:
        if influencer == influenced:
            continue
        infl_code = codes[influenced]

        subfolder_name = f"{inf_code}_{infl_code}"             #  ()"agr_cor"= Agriculture->Corruption) and ()"agr_eduq"=Agriculture->Education Quality)
        subfolder_path = os.path.join(influencer_folder, subfolder_name)
        os.makedirs(subfolder_path, exist_ok=True)

print("Research folder structure created successfully!") # If it is sucsuccessful, we print this line
