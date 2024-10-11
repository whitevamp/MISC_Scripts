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

def merge_json_files(start_file, folder_to_merge, log_file):
    """Merges JSON files and writes logs."""
    mod_count = 0
    total_mod_count = 0  # Track total mods added across all files
    file_counter = 1
    merged_data = read_json(start_file)  # Start with the base file
    mods_to_patch = merged_data.get("ModsToPatch", [])

    with open(log_file, 'w') as log:
        log.write(f"Merging mods starting from {start_file}\n")

        # Traverse the folder and merge each file
        for file_name in os.listdir(folder_to_merge):
            file_path = os.path.join(folder_to_merge, file_name)

            if file_name.endswith(".json"):
                try:
                    current_data = read_json(file_path)
                    mods_to_add = current_data.get("ModsToPatch", [])
                    log.write(f"Adding {len(mods_to_add)} mods from {file_name}. Total mods so far: {mod_count}\n")
                except json.JSONDecodeError:
                    log.write(f"Failed to add mods from {file_name} due to JSON error.\n")
                    continue  # Skip this file and move to the next one

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

#######

def main():
    start_file = "merged.json"  # Your base JSON file
    folder_to_merge = os.getcwd()  # Folder with JSON files
    #folder_to_merge = "mods_folder"  # Folder containing other JSON files to merge
    log_file = "merge_log.txt"  # Log file for recording the merge process
    
        # Check if the base file exists
    if not os.path.exists(start_file):
       print(f"Error: The file {start_file} was not found in {os.getcwd()}.")
       return
       
    # Ensure log file is empty at the start
    open(log_file, 'w').close()
    merge_json_files(start_file, folder_to_merge, log_file)

if __name__ == "__main__":
    main()
