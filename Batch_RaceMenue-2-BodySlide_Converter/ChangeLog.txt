Mod Description:

This script has been modified and expanded from the original version created by WolfKent. The key changes include improved error handling for missing bodyMorphs and keys, logging for skipped files, and additional customization options through command-line arguments. The script now recursively processes directories and outputs all files to a centralized directory, ensuring cleaner file management. The XML output is also beautified for readability.

Full credit for the original script goes WolfKent. Modifications were made to enhance usability and flexibility for broader use cases.



Here’s a detailed list of all the changes that were made to the original script to fix the issues and improve its functionality:

### 1. **Error Handling for Missing `keys` Attribute:**
   - **Original Script:**
     - It assumed the presence of the `keys` attribute in every `bodyMorph` entry.
     - The script would crash with a `KeyError` if any entry did not contain the `keys` field.

   - **Updated Script:**
     - **New Check Added:** `if 'keys' not in entry or not isinstance(entry['keys'], list)` was introduced to check if the `keys` attribute exists and ensure it is a list before proceeding.
     - **Error Logging for Missing `keys`:** If the `keys` field is missing, an error message is printed and logged using `log_error()` and the entry is skipped to prevent the script from crashing.
     - **Default Value for Missing `keys`:** If the `keys` field is missing, a default value of `0` is provided using:
       ```python
       body_morph.append({
           'name': e,
           'keys': [{'value': 0}]
       })
       ```

### 2. **Error Logging Function (`log_error`):**
   - **Original Script:**
     - Did not have a logging mechanism for errors.

   - **Updated Script:**
     - **New Function Added:** A new function `log_error(message)` was created to write error messages into an `error_log.txt` file located in the same directory as the script. This function helps track errors that occur during the execution of the script without halting the process.
     - **Error Messages Logged for Missing Data:** Error messages are logged for missing `keys`, missing `bodyMorphs`, and any issues related to JSON decoding.

### 3. **Handling Invalid or Corrupt JSON Files:**
   - **Original Script:**
     - The script did not handle cases where the JSON file was invalid or corrupted.

   - **Updated Script:**
     - **New Try-Except Block:** The `load_json()` function now contains a `try-except` block to catch `json.JSONDecodeError`, which logs an error and skips any invalid JSON file.
     - **Return `None` for Invalid JSON:** If the JSON parsing fails, the function returns `None` and the calling function skips the processing of that file. This prevents crashes due to malformed JSON.

### 4. **Missing `bodyMorphs` Handling:**
   - **Original Script:**
     - The script assumed the presence of the `bodyMorphs` node and would crash if it was missing.

   - **Updated Script:**
     - **Error Handling for Missing `bodyMorphs`:** The `try-except` block in the `convert_racemenu_2_bodyslide()` function now catches the `KeyError` raised when the `bodyMorphs` attribute is missing and logs an error message.
     - **Error Message and Logging:** The message `f"Skipping file due to missing 'bodyMorphs': {file_path}"` is printed and logged using the `log_error()` function.

### 5. **Ensure Directory Creation for Output Files:**
   - **Original Script:**
     - The script wrote the output files, but it did not ensure that the target directory `/output/CalienteTools/BodySlide/SliderPresets/` existed before trying to save the files, which could cause an error.

   - **Updated Script:**
     - **Directory Creation Check:** Before saving the output XML file, the script now checks if the target output directory exists using:
       ```python
       if not os.path.exists(output_dir):
           os.makedirs(output_dir)
       ```
     - **New Directory Creation:** If the directory doesn't exist, it is automatically created.

### 6. **Preserve XML Structure with `prettify()`:**
   - **Original Script:**
     - The script generated XML but did not apply any formatting to ensure the XML structure was readable.

   - **Updated Script:**
     - **New Function Added:** The `prettify()` function was added to pretty-print the XML output with indentation, making it easier to read and inspect the generated XML files. It uses `xml.dom.minidom` to format the XML before saving it.

### 7. **Skips Output Directory in Recursion:**
   - **Original Script:**
     - The script did not check for the `output` directory while recursively walking through directories, which might lead to processing the files it had just generated.

   - **Updated Script:**
     - **Skipping `output` Directory:** The line `if 'output' in dirs: dirs.remove('output')` was added to ensure the script skips over the `output` directory while recursively processing files. This prevents the script from processing files it has just generated, avoiding infinite loops or redundant processing.

### 8. **Command-line Argument Parsing and Defaults:**
   - **Original Script:**
     - The script had no command-line argument handling, and no flexibility for changing the size modifiers or names.

   - **Updated Script:**
     - **Optional Arguments:** The script can now accept up to four command-line arguments for `small_size_modifier`, `big_size_modifier`, `group_name`, and `body_name`. The script processes these arguments conditionally based on their number.
     - **Defaults:** If no arguments are provided, it falls back on default values: `small_size_modifier = 0.5`, `big_size_modifier = 1.5`, and uses the file name for `group_name` and `body_name` if not specified.

### 9. **Refactoring for Clarity and Reusability:**
   - **Original Script:**
     - The structure was somewhat linear and didn’t modularize functionality, making it harder to reuse parts of the code.

   - **Updated Script:**
     - **New Functions Added:** Functions like `load_json()`, `save_xml()`, `prettify()`, and `log_error()` were added to modularize and encapsulate key tasks, making the script easier to maintain and extend.
     - **Error Handling Modularization:** Error handling is now done through separate functions, allowing for cleaner and more maintainable code.

### 10. **Fallback for Missing Entries in `bodyMorph`:**
   - **Original Script:**
     - The script expected all entries from `bodyslide_elems` to be present in the `bodyMorphs` node.

   - **Updated Script:**
     - **Fallback Mechanism:** The script now adds missing elements from `bodyslide_elems` into `bodyMorph` with a default value:
       ```python
       body_morph.append({
           'name': e,
           'keys': [{'value': 0}]
       })
       ```
     - This ensures that even if some entries are missing from the input JSON, they are still processed and added to the output XML with default values.

### 11. **Enhanced XML Attribute Calculation for `size`:**
   - **Original Script:**
     - The script calculated size modifiers for sliders, but this logic was somewhat buried and harder to follow.

   - **Updated Script:**
     - **Size Modifier Logic Clarified:** The script now clearly distinguishes between `small` and `big` sizes when setting the values of `SetSlider`:
       ```python
       slider.attrib['value'] = str(round(value_new * small_size_modifier)) if size == "small" else str(value_new)
       ```

---

### Summary of Improvements:
- **Robustness**: The script now handles missing data and corrupt files without crashing, and logs errors for later review.
- **Modularity**: The code has been refactored into reusable functions, making it cleaner and easier to maintain.
- **Error Logging**: A new logging system tracks errors without disrupting the workflow.
- **Command-line Flexibility**: The script accepts command-line arguments for customization, improving usability.
- **Readable Output**: The XML output is now prettified for easy inspection.

These changes significantly improve the stability, flexibility, and maintainability of the script.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

If you use this code, please provide credit by including a reference to the original author.


ver1.1 changes.
added in more BodySlide options, to be completed. from sysdmp credits to them for the extra, BodySlide options
added in more error handling checks.