from pathlib import Path
file_contents = Path("RNU6_269P.txt").read_text()
header = file_contents.split("\n")[0]
print(header)