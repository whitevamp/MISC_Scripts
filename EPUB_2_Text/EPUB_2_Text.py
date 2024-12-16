from os import path, listdir
from zipfile import ZipFile
from bs4 import BeautifulSoup


FILE_NAME = "YOUR_FILE_NAME"
extract_dir = "EXTRACT_DIRECTORY"

with ZipFile(FILE_NAME, "r") as zip_ref:
    zip_ref.extractall(extract_dir)

for filename in listdir(extract_dir):
    if filename.endswith(".xhtml"): 
        print(filename)
        with open(path.join(extract_dir, filename), "r", encoding="utf-8") as f:
            soup = BeautifulSoup(f.read(), "lxml")
            for text_object in soup.find_all(text=True): 
                print(text_object)