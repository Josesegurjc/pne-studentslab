from Seq1 import Seq


# -- Create a Null sequence
s1 = Seq()

# -- Create a valid sequence
s2 = Seq("ACTGA")

# -- Create an invalid sequence
s3 = Seq("Invalid sequence")


def print_seqs(list_of_seq):
    for e in list_of_seq:
        index = list_of_seq.index(e)
        part1 = str(index) + ":"
        length = e.len(e.strbases)
        part2 = "(Length:" + str(length) + ")"
        print("Sequence", part1, part2, e)
        dict1 = e.seq_count(e.strbases)
        print(dict1)


list1 = [s1, s2, s3]
print_seqs(list1)
