import json
import os

mod_limit = 249  # Max number of mods per merged file

def read_json(file_path):
    """Reads JSON data from a file."""
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON in file: {file_path}")
        print(f"Error message: {e}")
        raise  # Re-raise the error after logging the problematic file

def write_json(file_path, data):
    """Writes JSON data to a file."""
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def read_txt(file_path):
    """Reads a plain text file and formats the content into a ModsToPatch list."""
    mods_to_patch = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                mod = line.strip()  # Remove any leading/trailing whitespace
                if mod:
                    mods_to_patch.append(mod)  # Add each mod to the list
    except Exception as e:
        print(f"Error reading text file: {file_path}. Error: {e}")
        raise
    return mods_to_patch

def merge_json_files(start_file, files_to_merge, log_file, file_format):
    """Merges either JSON or plain text files and writes logs."""
    mod_count = 0
    total_mod_count = 0  # Track total mods added across all files
    file_counter = 1
    merged_data = read_json(start_file)  # Start with the base JSON file
    mods_to_patch = merged_data.get("ModsToPatch", [])

    with open(log_file, 'w') as log:
        log.write(f"Starting the merge process. Base file: {start_file}\n")

        # Process each file to merge
        for file_to_merge in files_to_merge:
            log.write(f"\nProcessing file: {file_to_merge}\n")

            if file_format == "json":
                current_data = read_json(file_to_merge)
                mods_to_add = current_data.get("ModsToPatch", [])
            elif file_format == "txt":
                mods_to_add = read_txt(file_to_merge)  # Read and format from text file
                log.write(f"Read mods from plain text file: {file_to_merge}\n")
            else:
                log.write(f"Unsupported file format: {file_format}\n")
                continue

            log.write(f"Adding {len(mods_to_add)} mods from {file_to_merge}. Current mods: {mod_count}\n")

            # Check if adding these mods will exceed the limit
            while mods_to_add:
                space_left = mod_limit - mod_count

                # If the mods to add can fit within the limit
                if len(mods_to_add) <= space_left:
                    mods_to_patch.extend(mods_to_add)
                    mod_count += len(mods_to_add)
                    total_mod_count += len(mods_to_add)  # Update total mods count
                    mods_to_add = []  # All mods added
                else:
                    # If the mods exceed the limit, add only up to the limit
                    mods_to_patch.extend(mods_to_add[:space_left])
                    mod_count += space_left
                    total_mod_count += space_left  # Update total mods count

                    # Save the current file
                    merged_file_name = f"merged_{file_counter}.json"
                    merged_data["ModsToPatch"] = mods_to_patch
                    write_json(merged_file_name, merged_data)
                    log.write(f"Reached {mod_limit} mods, saving to {merged_file_name}\n")

                    # Start a new file for the remaining mods
                    file_counter += 1
                    mod_count = 0
                    mods_to_add = mods_to_add[space_left:]  # Remaining mods for next file
                    merged_data["ModsToPatch"] = []  # Reset mods for new file
                    mods_to_patch = []

        # Final save for remaining mods
        if mods_to_patch:
            merged_file_name = f"merged_{file_counter}.json"
            merged_data["ModsToPatch"] = mods_to_patch
            write_json(merged_file_name, merged_data)
            log.write(f"Final merged file saved to {merged_file_name}. Total mods: {mod_count}\n")

        # Log the overall total number of mods added across all merged files
        log.write(f"\nOverall total mods added across all merged files: {total_mod_count}\n")

def main():
    start_file = "merged.json"  # Template JSON file
    log_file = "merge_log.txt"  # Log file for recording the merge process

    # Check if the base file exists
    if not os.path.exists(start_file):
        print(f"Error: The file {start_file} was not found in {os.getcwd()}.")
        return

    # Ensure log file is empty at the start
    open(log_file, 'w').close()

    # Ask the user for the file format
    file_format = input("Enter the file format (json/txt): ").lower()

    if file_format not in ["json", "txt"]:
        print("Invalid file format. Please enter 'json' or 'txt'.")
        return

    # Automatically select files based on the chosen format
    files_to_merge = [f for f in os.listdir() if f.endswith(f".{file_format}")]
    if not files_to_merge:
        print(f"No {file_format} files found in the current directory.")
        return

    print(f"Found {len(files_to_merge)} {file_format} file(s) to merge: {files_to_merge}")

    # Merge the selected files
    merge_json_files(start_file, files_to_merge, log_file, file_format)

if __name__ == "__main__":
    main()
