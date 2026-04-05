import os

BASE_DIR = "."
DRY_RUN = False  # set to False when ready

def safe_rename(old_path, new_path):
    if old_path == new_path:
        return
    if os.path.exists(new_path):
        print(f"SKIP (target exists): {old_path} -> {new_path}")
        return
    if DRY_RUN:
        print(f"Would rename: {old_path} -> {new_path}")
    else:
        os.rename(old_path, new_path)
        print(f"Renamed: {old_path} -> {new_path}")

# Only look at the first level: variable directories inside research_repo
for variable_name in os.listdir(BASE_DIR):
    variable_path = os.path.join(BASE_DIR, variable_name)

    if not os.path.isdir(variable_path):
        continue

    # Look only at influence directories inside each variable directory
    for influence_name in os.listdir(variable_path):
        influence_path = os.path.join(variable_path, influence_name)

        if not os.path.isdir(influence_path):
            continue

        # Only fix names with double underscores
        if "__" in influence_name:
            new_name = influence_name.replace("__", "_")
            new_path = os.path.join(variable_path, new_name)
            safe_rename(influence_path, new_path)

print("Finished (dry-run mode)." if DRY_RUN else "Finished.")