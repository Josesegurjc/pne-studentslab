from Seq1 import Seq
list1 = [Seq("ACGTA")]
for e in list1:
    index = list1.index(e) + 1
    part1 = str(index) + ":"
    length = len(e.strbases)
    part2 = "(Length:" + str(length) + ")"
    print("Sequence", part1, part2, e)
