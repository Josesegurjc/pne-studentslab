from pathlib import Path
FILENAME = "Sequences/ADA.txt"
file_info = Path(FILENAME).read_text()
file_info = file_info[file_info.index("\n"):]
file_info = file_info.replace("\n", "")
print(len(file_info))
