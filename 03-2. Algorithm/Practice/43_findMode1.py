import random

ages = [random.randint(20, 50) for i in range(40)]
print(f'employee ages : {ages}')
print(f'employee cnt : {len(ages)}')

maxValue = 0
for a in ages:
    if maxValue < a:
        maxValue = a

mode = [0 for i in range(maxValue + 1)]
for a in ages:
    mode[a] += 1

print(f'max age : {maxValue}')
print(f'age mode : {mode}')

for i in range(len(mode)):
    maxValue = 0
    maxIndex = 0

    for j in range(len(mode)):
        if maxValue < mode[j]:
            maxValue = mode[j]
            maxIndex = j
            mode[j] = 0

    if maxValue == 0:
        break
    else:
        print(f'[{i if i > 9 else '0' + str(i)}]\t{maxIndex}세 빈도수: {maxValue} {'*' * maxValue} ')
