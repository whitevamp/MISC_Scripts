# Directory Structure Creator

This Python script provides a graphical user interface (GUI) to create customizable directory structures. It allows you to create multiple sets of directories, with the option to specify both primary and secondary directory structures, each with independently configurable depths.

## Features

- **Create Multiple Directory Sets**: Specify how many sets of directories you want to generate (e.g., `Replacer 1`, `Replacer 2`, etc.).
- **Customizable Directory Depth**: Configure the depth (number of nested directories) for each set.
- **Primary and Secondary Structures**: Optionally, add a secondary directory structure alongside the primary structure.
- **Dynamic Input Fields**: The UI dynamically adjusts to the depth you choose, allowing you to input custom names for each directory level.
- **Custom Output Location**: Select the base path where the directories will be created.
- **Error Handling**: Includes error checking to ensure valid inputs and handle unexpected issues.

## How to Use

### Requirements

- Python 3.x
- `tkinter` (Comes pre-installed with most Python installations)

### Instructions

1. **Clone or Download the Repository**:
   - Clone the repository using Git:
     ```bash
     git clone https://github.com/whitevamp/MISC_Scripts.git
     ```
   - Or download the `.zip` file from GitHub and extract it.

2. **Run the Script**:
   - Navigate to the directory where the script is located.
   - Run the script using Python:
     ```bash
     python directory_creator.py
     ```

3. **Using the UI**:
   - **Number of Directories**: Enter the number of directory sets you want to create (e.g., `Replacer 1`, `Replacer 2`, etc.).
   - **Base Path**: Use the "Browse" button to select the location where the directories will be created.
   - **Primary Directory Depth**: Select the depth (1-20) for the primary directory structure. Based on the depth, text fields will appear for you to input names for each level (e.g., `textures`, `interface`, `objects`).
   - **Secondary Directory Structure (Optional)**: 
     - Check the box labeled "Include secondary directory structure" to add a secondary directory set (e.g., `meshes`, `interface`, `logo`).
     - Select the depth (1-20) for the secondary directory and input names for each level.
   - **Create Directories**: Once everything is configured, click the "Create Directories" button to generate the directories.

4. **Example Output**:
   If you configure the following:
   - **Number of directories**: `3`
   - **Primary depth**: `4`
   - **Primary names**: `Replacer {n}`, `textures`, `interface`, `objects`
   - **Secondary depth**: `3`
   - **Secondary names**: `meshes`, `interface`, `logo`

   The script will generate the following directories:
\Replacer 1\textures\interface\objects 
\Replacer 1\meshes\interface\logo 
\Replacer 2\textures\interface\objects 
\Replacer 2\meshes\interface\logo 
\Replacer 3\textures\interface\objects 
\Replacer 3\meshes\interface\logo


## Error Handling

The script checks for:
- Missing or invalid input values.
- Invalid base paths or directory creation issues.
If any errors are encountered, an error message will appear to guide you in fixing the problem.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contributions

Feel free to fork this repository, open issues, or submit pull requests to improve the script or fix any bugs. All contributions are welcome!
