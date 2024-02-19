from Seq1 import Seq

s1 = Seq()

# -- Create a valid sequence
s2 = Seq("ACTGA")

# -- Create an invalid sequence
s3 = Seq("Invalid sequence")


def print_seqs(list1):
    for e in list1:
        index = list1.index(e) + 1
        part1 = str(index) + ":"
        length = e.len(e.strbases)
        part2 = "(Length:" + str(length) + ")"
        print("Sequence", part1, part2, e)

list1 = [s1, s2, s3]
print_seqs(list1)