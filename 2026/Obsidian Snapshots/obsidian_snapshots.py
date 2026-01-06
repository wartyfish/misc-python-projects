import os, zipfile, re
from pathlib import Path
from datetime import datetime, timedelta

target_path = Path(r"C:\Users\Eem\Dropbox\Jamies Vault")
destination_path = Path(r"P:\Obsidian vault backups")

create_snapshot = False

# date snapshot to yesterdays date
yesterdays_date = datetime.today() - timedelta(days=1)
snapshot_name = f"{yesterdays_date.strftime("%y%m%d")}_JamiesVaultSnapshot.zip"

# specify how frequently to make snapshots
interval_between_snapshots = 7

snapshots = list(destination_path.glob("*_JamiesVaultSnapshot.zip"))

# validate if any snapshots exist
# if not, proceed and create snapshot
# else, find date of most recent snapshot
if not snapshots:
    create_snapshot = True
else:
    latest_snapshot = max(snapshots)
    latest_snapshot_date = datetime.strptime(
    re.search(r"(\d{6})_JamiesVaultSnapshot\.zip", latest_snapshot.name).group(1),
    "%y%m%d"
    )
    days_since_last_snapshot = (yesterdays_date - latest_snapshot_date).days

    if days_since_last_snapshot >= interval_between_snapshots:
        create_snapshot = True

# create zipfile 
if create_snapshot:
    with zipfile.ZipFile(destination_path / snapshot_name, "w") as zipf:
        for root, dirs, files in os.walk(target_path):
            dirs[:] = [x for x in dirs if x != ".obsidian"]
            for file in files:
                full_path = Path(root) / file
                arcname = full_path.relative_to(target_path)
                zipf.write(full_path, arcname, compress_type=zipfile.ZIP_DEFLATED)

