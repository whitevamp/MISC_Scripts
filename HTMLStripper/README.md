# HTML Processor Script

## Overview

This script is a tool to recursively process HTML files from a selected directory, strip HTML and JavaScript content, perform spell-check, grammar-check, and format the plain text. The processed content can be saved in multiple formats including `.txt`, `.doc`, `.csv`, `.pdf`, `.epub`, `.html`, and `.htm`. You can also choose to output the content in all formats simultaneously.

Additionally, the script provides a progress bar in both the command-line interface (CLI) and the graphical user interface (GUI) to monitor the processing progress.

## Features

- **HTML & JavaScript Removal**: Strips HTML tags and JavaScript from the input files.
- **Spell Check**: Automatically corrects misspelled words using the `pyspellchecker` library.
- **Grammar Check**: Corrects grammar using `language_tool_python`.
- **Text Formatting**: Simple paragraph formatting applied to the stripped content.
- **Multiple Output Formats**: Supports output in `.txt`, `.doc`, `.csv`, `.pdf`, `.epub`, `.html`, and `.htm` formats.
- **All Formats Option**: Option to save the output in all available formats simultaneously.
- **Progress Bar**: Displays a progress bar in both the GUI and CLI during file processing.

## Requirements

To use this script, you need to have the following Python libraries installed:

```txt
beautifulsoup4
docx
pandas
fpdf
ebooklib
language-tool-python
pyspellchecker
tqdm
tkinter
```


Usage

    Clone or download this repository.

    Install the required dependencies using the requirements.txt file:

    bash

pip install -r requirements.txt

Run the script:

bash

python html_processor.py

The GUI will open where you can:

    Select the input directory containing the HTML files.
    Select the output directory for the processed files.
    Choose the desired output format or select All Formats to save the files in all formats.
    Click Start to begin processing.

The progress of the file processing will be shown both in the GUI and the command-line terminal.
