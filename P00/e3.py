from Seq0 import seq_len
from Seq0 import seq_read_fasta
list_of_sequences = ["U5", "ADA", "FRAT1", "FXN"]
for e in list_of_sequences:
    seq = seq_read_fasta(e)
    length = seq_len(seq)
    print("Gene", e, "-> Length:", length)
