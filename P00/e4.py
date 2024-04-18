from Seq0 import seq_count_base
from Seq0 import seq_read_fasta
list_of_sequences = ["U5", "ADA", "FRAT1", "FXN"]
list_of_bases = ["A", "C", "T", "G"]
for e in list_of_sequences:
    filename = "Sequences/" + e + ".txt"
    seq = seq_read_fasta(filename)
    print("Gene", e + ":")
    for c in list_of_bases:
        print(c + ":", seq_count_base(seq, c))
