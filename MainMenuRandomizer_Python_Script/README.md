```markdown
# Main Menu Randomizer & Game Start

## Overview

**Main Menu Randomizer & Game Start** is a Python script designed to randomly select a file from a specified source directory and copy it to a designated destination folder. It also launches a specified executable (such as a game) after the file is copied. This tool is particularly useful for modders who want to manage assets dynamically in their games.

## Features

- Randomly selects a file from a source directory.
- Copies the selected file to a specified destination folder, overwriting any existing files.
- Launches a specified executable after copying the file.
- Configurable through a simple configuration file.
- Command line argument support for specifying the location of the config file.
- Exception handling for better user experience.

## Installation

### Prerequisites

- Python 3.x
- Required Python packages:
  - `os`
  - `random`
  - `shutil`
  - `configparser`

You can install the required packages using pip:

```bash
pip install configparser
```

### Using the Script

1. **Clone the repository** or download the script files.

   ```bash
   git clone https://github.com/whitevamp/MISC_Scripts.git
   ```

2. **Configure the Script**:
   - Create a configuration file named `config.ini` in the same directory as the script or specify its path via command line.
   - The config file should contain the following:

   ```ini
   [Paths]
   source_dir=C:\\path\\to\\your\\source
   dest_dir=C:\\path\\to\\your\\destination
   new_file_name=new_file_name.extension
   program_path=C:\\path\\to\\your\\program.exe
   ```

   Ensure to use double backslashes (`\\`) in file paths.

3. **Run the Script**:
   - You can run the script using the command line. If you want to specify a different configuration file, use the following syntax:

   ```bash
   python MainMenuRandomizer.py -c "path/to/custom_config.ini"
   or
   python MainMenuRandomizer.py --config "path/to/custom_config.ini"
   ```

   If no argument is provided, the script will look for the `config.ini` file in the current working directory.

## Creating an Executable

To convert the Python script into an executable, you can use `PyInstaller`. Follow these steps:

1. **Install PyInstaller**:

   ```bash
   pip install pyinstaller
   ```

2. **Create the Executable**:
   - Navigate to the directory where your script is located and run:

   ```bash
   pyinstaller --onefile --icon=path_to_icon.ico MainMenuRandomizer.py
   ```

   Replace `path_to_icon.ico` with the path to your desired icon file.

3. **Locate the Executable**:
   - After running the command, the executable will be found in the `dist` directory within your project folder.

## Usage with Mod Organizer 2 (MO2)

1. Install the mod like any other and ensure it is enabled in MO2.
2. To add to MO2, In the upper right section where you select SKSE, choose edit, then click the "+" in the upper left corner, select "Add from file," and navigate to where you installed the mod.
3. In MO2, right-click on a mod, then select **All Mods**, create an empty mod, and name it as you wish, then activate it.
4. Change the following lines in `config.ini` to point to your source files, destination folder, and executable:

   ```
     source_dir = C:\\path\\to\\source\\folder
     dest_dir = C:\\path\\to\\destination\\folder
     new_file_name = newname.dds
     program_path = C:\\path\\to\\your\\program.exe
   ```
### Notes:

you have to use double \\ in the config file.
For MO2 you may also need to add "start in" path and also set "Arguments" -c "path/to/custom_config.ini", when setting it as an executable in MO2.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
