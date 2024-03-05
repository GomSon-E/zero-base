def findMax(data):
    maxValue = 0
    for d in data:
        if maxValue < d:
            maxValue = d

    maxCnt = 0
    for d in data:
        if d == maxValue:
            maxCnt += 1

    print(f'max value : {maxValue}')
    print(f'max count : {maxCnt}')


import random

nums = [random.randint(1, 50) for i in range(30)]
print(f'nums : {nums}')

findMax(nums)