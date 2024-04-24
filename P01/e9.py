from Seq1 import Seq

s1 = Seq()
s1 = s1.seq_read_fasta("Sequences/U5")
list_of_seq = [s1]
for e in list_of_seq:
    index = list_of_seq.index(e)
    part1 = str(index) + ":"
    length = e.len(e.strbases)
    part2 = "(Length:" + str(length) + ")"
    print("Sequence", part1, part2, e)
    dict1 = e.seq_count(e.strbases)
    print(dict1)
    reverse = e.seq_reverse(e.strbases)
    print("Rev:", reverse)
    complementary = e.seq_complement(e.strbases)
    print("Comp:", complementary)
