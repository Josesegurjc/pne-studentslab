from pathlib import Path
file_info = Path("Sequences/ADA.txt").read_text()
file_info = file_info[file_info.index("\n"):]
file_info = file_info.replace("\n", "")
print(len(file_info))

