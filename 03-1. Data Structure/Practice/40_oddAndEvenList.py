import random

randomList = random.sample(range(1, 101), 10)

evenList = []
oddList = []

for i in randomList:
    if i % 2 == 0:
        evenList.append(i)
    else:
        oddList.append(i)

print(f'짝수: {evenList}, 개수: {len(evenList)}개')
print(f'홀수: {oddList}, 개수: {len(oddList)}개')