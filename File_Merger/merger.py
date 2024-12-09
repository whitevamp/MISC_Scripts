import os

# Get list of txt files in the current directory
files = [f for f in os.listdir() if f.endswith('.txt')]

# Sort the files numerically based on the number in the filename
files.sort(key=lambda x: int(x.split('.')[0]))

# Write the contents of the sorted files into merged.txt
with open('merged.txt', 'w', encoding='utf-8', errors='ignore') as merged_file:
    for file in files:
        with open(file, 'r', encoding='utf-8', errors='ignore') as f:
            merged_file.write(f.read())
            merged_file.write("\n")  # Add a newline between file contents
