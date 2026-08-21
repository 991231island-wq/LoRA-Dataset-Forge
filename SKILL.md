---
name: lora-dataset-forge
description: >
  A skill for preparing LoRA editing model datasets.
  It merges START-END paired datasets, prevents filename collisions,
  preserves training platform naming conventions, and generates reports.
---

# LoRA Dataset Forge

## Purpose
Prepare LoRA editing datasets from multiple training packages.

## Supported format

Input:
- 0001_start.png
- 0001_end.png
- 0001.txt

Output:
- 010001_start.png
- 010001_end.png
- 010001.txt

The first two digits represent the source dataset id.

## Workflow

1. Inspect dataset structure.
2. Check start/end/txt matching.
3. Merge datasets.
4. Rename safely.
5. Generate merge report.
