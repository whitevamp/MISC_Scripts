# SLAX KeyWords Patcher - Merge Mods to Patch Python Script

This repository contains two simple Python scripts I created to automate the process of making SLAX KeyWords patches for a Synthesis patcher. These scripts streamline the mod file selection process by creating `settings.json` files for use in the Synthesis patcher, reducing the manual effort of selecting mod files.

## Features

- **Template File Duplication**: The scripts take a template file and copy its contents into a new file.
- **Mod List Processing**: They then read a list of mods from a given input file, which can be either a `.txt` or `.json` file. Each line in the input file is considered a mod.
- **Mod Limit**: The scripts enforce a mod limit of 249 mods per merged file (configurable by modifying the `mod_limit` variable in the script). This is slightly below the 254 mod limit, allowing for some leeway.
- **Log Output**: After merging, the scripts generate a log file summarizing the total number of mods added across all output files.
- **Two Versions Available**:
  - `MergeModsToPatchWFileTypeSelection.py`: Asks for your preferred input format (`json` or `txt`).
  - `MergeModsToPatch-no-type-selection.py`: Only accepts `.json` files as input.

## Input Formats

### JSON Example

The JSON file should follow this format, with mods listed under the `ModsToPatch` key:

```json
{
  "kwdSettings": {
    "ArmorHarnessDefault": true,
    "ArmorIllegalDefault": true,
    "ArmorLewdLeotardDefault": true,
    "ArmorPartBottomDefault": true,
    "ArmorPartTopDefault": true,
    "ArmorPrettyDefault": true
  },
  "modstopatchSettings": {
    "ModsToPatch": [
      // Your mods go here
    ]
  }
}
```

### TXT Example

The `.txt` file should list each mod file on a new line, like so:

```
[full_inu] Queen Marika's Dress.esp
KSO Mage Robes.esp
KSO Mage Robes ACE.esp
(Code Vein) Eva.esp
[Dyuz] Highclass Jian.esp
[Cloud] Daki.esp
[Rand] ESO Corseted Riding Outfit.esp
[Rand] GW2 Eir Set.esp
[Rand] Mixed Monk Set.esp
[Rand] Yakaku Set.esp
[FarliBarcai] GTA Bikini.esp
[full_inu] Armor Pack 01.esp
```

## Error Handling and Logging

Both scripts include basic error handling and logging. After processing the mods, the scripts generate a log file that shows the total number of mods added across all output files. For example, if the output consists of two files, the log may contain the following:

```
Overall total mods added across all merged files: 446
```

## Why Two Versions?

The primary difference between the two Python scripts is that `MergeModsToPatchWFileTypeSelection.py` asks you which input file format you'd like to use (`json` or `txt`), while `MergeModsToPatch-no-type-selection.py` skips this prompt and only processes `.json` files.

I kept both versions for convenience. Even though `MergeModsToPatchWFileTypeSelection.py` is arguably more flexible, I decided not to delete the simpler version.

## How to Use

1. Clone or download this repository.
2. Place the scripts in the directory where your mod files are located.
3. For `MergeModsToPatchWFileTypeSelection.py`, run the script and choose your input file type when prompted (`json` or `txt`).
4. For `MergeModsToPatch-no-type-selection.py`, ensure your input file is in `.json` format.
5. The scripts will recursively read the input files and generate merged output files up to the `mod_limit`.

You can modify the mod limit by changing the following line in the script:

```python
mod_limit = 249  # Max number of mods per merged file
```

## Sample Input Files

A sample `.json` file is provided in the repository, which follows the format I used for my SLAX KeyWords patches. You can customize it to fit your modding needs.

## License

Feel free to use, modify, and distribute this script as needed. This project is provided "as is," without any warranty.