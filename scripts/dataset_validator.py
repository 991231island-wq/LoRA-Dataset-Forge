from pathlib import Path


def validate_dataset(folder):
    folder = Path(folder)

    samples = {}

    for file in folder.iterdir():
        stem = file.stem

        if "_start" in stem:
            key = stem.replace("_start", "")
            samples.setdefault(key, {})["start"] = file

        elif "_end" in stem:
            key = stem.replace("_end", "")
            samples.setdefault(key, {})["end"] = file

        elif file.suffix.lower() == ".txt":
            samples.setdefault(stem, {})["txt"] = file

    report = {
        "total_samples": len(samples),
        "missing_start": [],
        "missing_end": [],
        "missing_txt": []
    }

    for key, item in samples.items():
        if "start" not in item:
            report["missing_start"].append(key)

        if "end" not in item:
            report["missing_end"].append(key)

        if "txt" not in item:
            report["missing_txt"].append(key)

    return report
