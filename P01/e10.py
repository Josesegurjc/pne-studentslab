from Seq1 import Seq
list_of_names = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
i = 0
list2 = []
for e in list_of_names:
    filename = "Sequences/" + e
    s = Seq()
    s = s.seq_read_fasta(filename)
    base = s.most_common_base(s.strbases)
    print("Gene", list_of_names[i], ":", "Most frequent Base:", base)
    i += 1
    