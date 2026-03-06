import os

BASE_DIR = "Research"

OLD_TEXT = "Religion"
NEW_TEXT = "Spirituality-God"

DRY_RUN = False  # set to False to apply changes

def safe_rename(old_path, new_path):
    if old_path == new_path:
        return
    if DRY_RUN:
        print(f"Would rename: {old_path} → {new_path}")
    else:
        os.rename(old_path, new_path)

for root, dirs, files in os.walk(BASE_DIR, topdown=False):

    # ----- FILE CONTENTS -----
    for name in files:
        old_path = os.path.join(root, name)

        # Skip PDFs and binaries
        if name.lower().endswith(".pdf"):
            continue

        try:
            with open(old_path, "r", encoding="utf-8") as f:
                content = f.read()
        except:
            continue

        if OLD_TEXT in content:
            if DRY_RUN:
                print(f"Would update text in: {old_path}")
            else:
                with open(old_path, "w", encoding="utf-8") as f:
                    f.write(content.replace(OLD_TEXT, NEW_TEXT))

        # ----- FILE RENAMES -----
        new_name = name
        if new_name.endswith("_rel"):
            new_name = new_name[:-4] + "_spi"
        if new_name.startswith("rel_"):
            new_name = "spi_" + new_name[4:]

        if new_name != name:
            safe_rename(old_path, os.path.join(root, new_name))

    # ----- DIRECTORY RENAMES -----
    for name in dirs:
        old_dir = os.path.join(root, name)
        new_name = name

        if new_name.endswith("_rel"):
            new_name = new_name[:-4] + "_spi"
        if new_name.startswith("rel_"):
            new_name = "spi_" + new_name[4:]

        if new_name != name:
            safe_rename(old_dir, os.path.join(root, new_name))

print("✅ Finished (dry-run mode)." if DRY_RUN else "✅ Finished.")
