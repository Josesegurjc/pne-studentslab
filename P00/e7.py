from Seq0 import seq_complement
from Seq0 import seq_read_fasta
filename = "U5.txt"
string = seq_read_fasta(filename)[:19]
complement = seq_complement("U5")[:19]
print("Gene U5:")
print("Frag:", string)
print("Comp:", complement)