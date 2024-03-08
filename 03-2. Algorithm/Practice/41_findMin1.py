def findMax(data):
    minValue = 0
    for d in data:
        if minValue == 0 or minValue > d:
            minValue = d

    minCnt = 0
    for d in data:
        if d == minValue:
            minCnt += 1

    print(f'max value : {minValue}')
    print(f'max count : {minCnt}')


import random

nums = [random.randint(1, 50) for i in range(30)]
print(f'nums : {nums}')

findMax(nums)