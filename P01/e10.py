from Seq1 import Seq
s1 = Seq()
s1 = s1.seq_read_fasta("U5")
s2 = Seq()
s2 = s2.seq_read_fasta("ADA")
s3 = Seq()
s3 = s3.seq_read_fasta("FRAT1")
s4 = Seq()
s4 = s1.seq_read_fasta("FXN")
s5 = Seq()
s5 = s1.seq_read_fasta("RNU6_269P")
list1 = [s1, s2, s3, s4, s5]
list_of_names = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
i = 0
for e in list1:
    base = e.most_common_base(e.strbases)
    print("Gene", list_of_names[i], ":", "Most frequent Base:", base)
    i += 1