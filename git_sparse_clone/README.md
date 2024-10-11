# Git Sparse Clone Python Script

This Python script clones a Git repository using a **sparse checkout**. Instead of cloning the entire repository, the script allows you to specify only the files or directories you need, saving time and space.

## Features

- **Sparse Checkout**: Clone only specific files or directories from a Git repository.
- **Dynamic Default Branch Detection**: Automatically detects and pulls from the repository's default branch (`main`, `master`, etc.).
- **Cross-Platform**: Works on any platform that supports Python and Git.
- **Error Handling**: Includes error handling for common Git and OS issues.

## Prerequisites

- **Python**: Ensure Python 3.x is installed.
- **Git**: Ensure Git is installed and accessible from the command line.

## Installation

1. Clone or download this repository.
2. Ensure you have both Python and Git installed on your system.
3. Save the `git_sparse_clone.py` script in a directory of your choice.

## Usage

The script accepts three main arguments: the repository URL, the local directory to clone into, and the file(s)/folder(s) to include in the sparse checkout.

### Syntax

```bash
python git_sparse_clone.py <repo_url> "<local_directory>" <file_or_folder1> <file_or_folder2> ...
```

### Example

To clone only specific files or directories from a repository:

```bash
python git_sparse_clone.py https://github.com/USER/REPO_NAME.git "localfolder" remote/file/folder1 remote/file/folder2
```

In this example:
- `https://github.com/USER/REPO_NAME.git` is the repository URL.
- `"localfolder"` is the local directory where the repository will be cloned.
- `remote/file/folder1` and `remote/file/folder2` are the files or directories to include in the sparse checkout.

### Notes
- Ensure the paths for the remote files/folders are correct and relative to the root of the repository.
- The script will automatically detect the repository's default branch and pull from it.

## How It Works

1. **Initialize**: Creates the local directory and initializes a Git repository in it.
2. **Add Remote**: Adds the remote repository URL.
3. **Enable Sparse Checkout**: Enables sparse checkout, which limits what is cloned.
4. **Add Sparse Files/Folders**: Writes the specified files or directories to the sparse-checkout configuration.
5. **Pull from Default Branch**: Detects the repository’s default branch (e.g., `main` or `master`) and pulls only the specified files or directories.

## Error Handling

The script includes error handling for:
- **Git Operation Errors**: If any Git command fails, it will output an error message and stop the process.
- **File/OS Errors**: Handles issues like missing directories or inaccessible paths.
- **Unexpected Errors**: Any other exceptions are caught and displayed with a relevant message.

## Modifying the Script

You can easily modify the script if you need to adjust the behavior, such as changing the default branch name or adding more advanced Git configurations.

## License

This script is open source and available under the MIT License. Feel free to use, modify, and distribute it as needed.