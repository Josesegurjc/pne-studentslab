from Seq0 import seq_complement
from Seq0 import seq_read_fasta
filename = "Sequences/U5"
string = seq_read_fasta(filename)[:19]
complement = seq_complement(string)[:19]
print("Gene U5:")
print("Frag:", string)
print("Comp:", complement)