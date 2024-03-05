def recursiveFunction(n1, n2):
    if n1 < n2:
        nextNum = n1 + 1
    else:
        nextNum = n1 - 1

    if nextNum == n2:
        return 0
    else:
        return nextNum + recursiveFunction(nextNum, n2)


num1 = int(input('input number1: '))
num2 = int(input('input number2: '))
print(recursiveFunction(num1, num2))