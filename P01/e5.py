from Seq1 import Seq


# -- Create a Null sequence
s1 = Seq()

# -- Create a valid sequence
s2 = Seq("ACTGA")

# -- Create an invalid sequence
s3 = Seq("Invalid sequence")


list_of_seq = [s1, s2, s3]
for e in list_of_seq:
    index = list_of_seq.index(e)
    part1 = str(index) + ":"
    length = e.len(e.strbases)
    part2 = "(Length:" + str(length) + ")"
    print("Sequence", part1, part2, e)
    dict1 = e.seq_count(e.strbases)
    print("A:", dict1["A"], " C:", dict1["C"], " T:", dict1["T"], " G:", dict1["G"])
