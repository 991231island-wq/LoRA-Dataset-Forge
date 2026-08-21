# LoRA Dataset Forge

A dataset engineering toolkit for LoRA editing models.

Build, validate and merge START-END paired training datasets while preserving
training platform naming conventions.

## Features

- Merge multiple START-END LoRA training packages
- Preserve start/end/txt pairing rules
- Automatic dataset ID naming
- Detect missing start/end/caption files
- Generate dataset reports

## Supported Format

Input:

```
0001_start.png
0001_end.png
0001.txt
```

Merged output:

```
010001_start.png
010001_end.png
010001.txt
```

Naming rule:

- First two digits: dataset source ID
- Last four digits: sample ID

## Roadmap

- Web UI
- Dataset preview
- Automatic quality scoring
- ModelScope Space integration
