def fibon(n):
    list_of_numbers = [0, 1]
    for i in range(0, n - 1):
        n3 = list_of_numbers[i] + list_of_numbers[i + 1]
        list_of_numbers.append(n3)
    print(str(n) + "th", "Fibonacci term:", list_of_numbers[-1])


fibon(5)
fibon(10)
fibon(15)
