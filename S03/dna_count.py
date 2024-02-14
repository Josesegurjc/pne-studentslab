sequence = input("Enter a sequence:")
countA = 0
countC = 0
countG = 0
countT = 0
for e in sequence:
    if e == "A":
        countA += 1
    if e == "C":
        countC += 1
    if e == "G":
        countG += 1
    if e == "T":
        countT += 1
print("Total length:", len(sequence))
print("A:", countA)
print("C:", countC)
print("T:", countT)
print("G:", countG)
