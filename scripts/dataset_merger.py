from pathlib import Path
import os
import shutil


def merge_datasets(input_folders, output_folder):
    output = Path(output_folder)
    output.mkdir(parents=True, exist_ok=True)

    logs = []

    for dataset_id, folder in enumerate(input_folders, start=1):
        dataset_prefix = str(dataset_id).zfill(2)

        for root, _, files in os.walk(folder):
            for filename in files:
                src = Path(root) / filename

                if src.suffix.lower() not in [
                    ".png", ".jpg", ".jpeg", ".webp", ".txt"
                ]:
                    continue

                stem = src.stem
                ext = src.suffix
                parts = stem.split("_")

                if len(parts) >= 2 and parts[0].isdigit():
                    new_name = (
                        dataset_prefix +
                        parts[0].zfill(4) +
                        "_" +
                        "_".join(parts[1:]) +
                        ext
                    )
                else:
                    new_name = dataset_prefix + stem + ext

                target = output / new_name

                count = 1
                while target.exists():
                    target = output / f"{target.stem}_{count}{ext}"
                    count += 1

                shutil.copy2(src, target)
                logs.append(f"{src.name} -> {target.name}")

    return logs
