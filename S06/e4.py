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


def generate_seqs(pattern, number):
    string = ""
    i = 0
    list1 = []
    while i < number:
        string += pattern
        i += 1
        list1.append(Seq(string))
    return list1


def print_seqs(list1, color):
    import termcolor
    for e in list1:
        index = list1.index(e)
        length = len(e.strbases)
        string = "Sequence " + str(index) + ": " + "(Length: " + str(length) + ")" + str(e)
        termcolor.cprint(string, color)


seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)

print("List 1:")
print_seqs(seq_list1, "blue")

print()
print("List 2:")
print_seqs(seq_list2, "green")
