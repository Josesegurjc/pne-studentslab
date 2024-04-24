list_of_numbers = [0, 1]
for i in range(0, 9):
    n3 = list_of_numbers[i] + list_of_numbers[i + 1]
    list_of_numbers.append(n3)
for e in list_of_numbers:
    print(e, end=" ")
