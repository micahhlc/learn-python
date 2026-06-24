import os
import argparse

# --- CLI argument setup ---
parser = argparse.ArgumentParser(
  description="Rename files in a folder by replacing a filename prefix.",
  epilog=(
      "Examples:\n"
      "  python fileUpdate.py              # preview only (dry run)\n"
      "  python fileUpdate.py -f           # dry run = false. actually rename files\n"
      "  python fileUpdate.py --force      # same as -f\n"
  ),
  formatter_class=argparse.RawTextHelpFormatter  # preserves newlines in epilog
)
parser.add_argument("-f", "--force", action="store_true", help="Actually rename (default is dry run)")
args = parser.parse_args()

# --- config ---
folder = "/Users/micah.cheng/Library/CloudStorage/Box-Box/My Box Notes/ScreenShots"
old_prefix = "Screenshot"
new_prefix = "employee_mgt_training"
dry_run = not args.force
# --------------

files = os.listdir(folder)

for filename in files:
  if filename.startswith(old_prefix):
    new_name = filename.replace(old_prefix, new_prefix, 1)
    old_path = os.path.join(folder, filename)
    new_path = os.path.join(folder, new_name)

    if dry_run:
        print(f"[DRY RUN] {filename}  →  {new_name}")
    else:
        os.rename(old_path, new_path)
        print(f"Renamed: {filename}  →  {new_name}")

print("\nDone." if not dry_run else "\nSet -f flag to apply.")