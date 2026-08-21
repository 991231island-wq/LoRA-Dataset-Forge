import os
import shutil
from pathlib import Path
from datetime import datetime


def merge_datasets(input_folders, output_folder):
    output = Path(output_folder)
    output.mkdir(parents=True, exist_ok=True)

    logs = []

    for dataset_id, folder in enumerate(input_folders, start=1):
        for root, _, files in os.walk(folder):
            for filename in files:
                src = Path(root) / filename

                if src.suffix.lower() not in [".png", ".jpg", ".jpeg", ".webp", ".txt"]:
                    continue

                stem = src.stem
                ext = src.suffix

                parts = stem.split("_")

                if len(parts) >= 2 and parts[0].isdigit():
                    new_stem = (
                        str(dataset_id).zfill(2)
                        + parts[0].zfill(4)
                        + "_"
                        + "_".join(parts[1:])
                    )
                else:
                    new_stem = str(dataset_id).zfill(2) + stem

                target = output / (new_stem + ext)

                counter = 1
                while target.exists():
                    target = output / f"{new_stem}_{counter}{ext}"
                    counter += 1

                shutil.copy2(src, target)
                logs.append(f"{src.name} -> {target.name}")

    with open(output / "merge_log.txt", "w", encoding="utf-8") as f:
        f.write("LoRA Dataset Forge Report\n")
        f.write(str(datetime.now()))
        f.write("\n\n")
        f.write("\n".join(logs))

    return logs
