class Seq:
    """A class for representing sequences"""
    def __init__(self, strbases):
        self.strbases = strbases
        condition = True
        correct_letters = "ACGT"
        for e in strbases:
            if not(e in correct_letters):
                condition = False
        if condition:
            print("New sequence created!")
        else:
            print("ERROR!!")

    def __str__(self):
        condition = True
        correct_letters = "ACGT"
        for e in self.strbases:
            if not (e in correct_letters):
                condition = False
        if condition:
            string = self.strbases
        else:
            string = "ERROR"
        return string

    def len(self):
        return len(self.strbases)


def print_seqs(list1):
    for e in list1:
        index = list1.index(e)
        part1 = str(index) + ":"
        length = len(e.strbases)
        part2 = "(Length:" + str(length) + ")"
        print("Sequence", part1, part2, e)


seq_list = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]
print_seqs(seq_list)
