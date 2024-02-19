from pathlib import Path
file_info = Path("Sequences/U5.txt").read_text()
file_info = file_info.split("\n")[1:]
print("Body of the U5.txt file:")
for e in file_info:
    print(e, "")