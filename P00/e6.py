from Seq0 import seq_reverse
from Seq0 import seq_read_fasta
filename = "U5.txt"
string = seq_read_fasta(filename)[:19]
reverse = seq_reverse("U5", 20)
print("Gene U5")
print("Fragment:", string)
print("Reverse", reverse)
