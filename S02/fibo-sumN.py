def fibosum(n):
    list_of_numbers = [0, 1]
    count = 0
    for i in range(0, n - 1):
        n3 = list_of_numbers[i] + list_of_numbers[i + 1]
        list_of_numbers.append(n3)
    for e in list_of_numbers:
        count += e
    print("Sum of the First", n, "terms of the Fibonacci series:", count)


fibosum(5)
fibosum(10)
