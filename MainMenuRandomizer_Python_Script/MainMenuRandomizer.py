import os
import sys
import shutil
import time
import configparser
import random
import argparse

# Set up argument parsing for specifying the config file location
parser = argparse.ArgumentParser(description='Main Menu Randomizer')
parser.add_argument('-c', '--config', help='Specify the path to the config file', default='config.ini')
args = parser.parse_args()

config_file = args.config

# Load configuration from the specified config file, or the default one if none is specified
config = configparser.ConfigParser()
config.read(config_file)

try:
    source_dir = config.get('Settings', 'source_dir')
    dest_dir = config.get('Settings', 'dest_dir')
    new_file_name = config.get('Settings', 'new_file_name')
    program_path = config.get('Settings', 'program_path')

    # Validate the provided paths and filenames
    if not os.path.isdir(source_dir):
        raise ValueError(f"source_dir is not set correctly: {source_dir}")
    if not os.path.isdir(dest_dir):
        raise ValueError(f"dest_dir is not set correctly: {dest_dir}")
    if not new_file_name:
        raise ValueError("new_file_name is not set correctly.")
    if not os.path.isfile(program_path):
        raise ValueError(f"program_path is not set correctly: {program_path}")

    # Clean destination folder (delete all files)
    for file_name in os.listdir(dest_dir):
        file_path = os.path.join(dest_dir, file_name)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f"Failed to delete {file_path}: {e}")
            raise

    # Randomly pick a file from source_dir
    source_files = [f for f in os.listdir(source_dir) if os.path.isfile(os.path.join(source_dir, f))]
    if not source_files:
        raise FileNotFoundError("No files found in the source directory.")

    selected_file = os.path.join(source_dir, random.choice(source_files))  # Randomly selects a file
    
    # Copy the selected file to the destination folder and rename it
    destination_file = os.path.join(dest_dir, new_file_name)
    shutil.copy2(selected_file, destination_file)

    print(f"Copied and renamed {selected_file} to {destination_file}")

    # Adding a wait before starting the program to ensure all file operations are complete
    time.sleep(5)

    # Launch the program (e.g., Skyrim or another executable)
    os.startfile(program_path)

except configparser.NoOptionError as no_option_err:
    print(f"Configuration error: {no_option_err}")
    sys.exit(1)
except FileNotFoundError as fnf_error:
    print(f"File error: {fnf_error}")
    sys.exit(1)
except ValueError as value_error:
    print(f"Value error: {value_error}")
    sys.exit(1)
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    sys.exit(1)
