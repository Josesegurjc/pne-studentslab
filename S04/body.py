from pathlib import Path
FILENAME = "Sequences/U5.txt"
file_info = Path(FILENAME).read_text()
file_info = file_info[file_info.find("\n"):]
print("Body of the U5.txt file:")
print(file_info)