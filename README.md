# LoRA Dataset Forge

A ModelScope Skill for LoRA editing model dataset management.

## Features

- Merge multiple START-END training packages
- Preserve start/end pairing rules
- Avoid filename conflicts
- Detect missing files
- Generate merge logs

## Example

Input:

0001_start.png
0001_end.png
0001.txt

Output:

010001_start.png
010001_end.png
010001.txt

## Roadmap

- Web UI
- Dataset preview
- Automatic quality scoring
- ModelScope Space integration
