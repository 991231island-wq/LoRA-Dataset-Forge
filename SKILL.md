---
name: lora-dataset-forge
description: >
  A dataset engineering skill for LoRA editing models.
  It merges, validates and organizes START-END paired training datasets.
---

# LoRA Dataset Forge

## When to use this skill

Use this skill when users need:

- Merge multiple LoRA editing datasets
- Fix duplicate training filenames
- Validate START-END image pairs
- Prepare datasets for LoRA training

## Supported dataset format

Example:

0001_start.png
0001_end.png
0001.txt

Output:

010001_start.png
010001_end.png
010001.txt

## Workflow

1. Inspect dataset structure.
2. Validate image pairs.
3. Assign dataset IDs.
4. Merge datasets safely.
5. Generate reports.
