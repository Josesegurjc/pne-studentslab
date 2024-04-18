from pathlib import Path
FILENAME = "Sequences/RNU6_269P.txt"
file_contents = Path(FILENAME).read_text()
header = file_contents[:file_contents.find("\n")]
print("First line of the RNU6_269P.txt file:")
print(header)