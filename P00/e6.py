from Seq0 import seq_reverse
from Seq0 import seq_read_fasta
filename =  "Sequences/U5"
seq = seq_read_fasta(filename)[:20]
reverse = seq_reverse(seq, 20)
print("Gene U5")
print("Fragment:", seq)
print("Reverse:", reverse)
