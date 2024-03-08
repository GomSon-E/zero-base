numberList = [2, 22, 7, 8, 9, 2, 7, 3, 5, 2, 7, 1, 3]
print(f'numberList : {numberList}')

i = 0
while True:
    if i >= len(numberList):
        break

    number = numberList[i]

    if numberList.count(number) >= 2:
        numberList.remove(number)
    else:
        i += 1

print(f'numberList : {numberList}')