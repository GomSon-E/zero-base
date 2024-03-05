def numberRanking(data):
    ranks = [0 for i in range(len(data))]

    for i, n1 in enumerate(data):
        for j, n2 in enumerate(data):
            if n1 < n2:
                ranks[i] += 1

    print(f'ranks : {ranks}')

    sortedRanks = []

    for i, n1 in enumerate(data):
        for j, n2 in enumerate(ranks):
            if i == n2:
                sortedRanks.append(data[j])
                break

    print(f'sorted ranks : {sortedRanks}')


import random

nums = random.sample(range(50, 101), 20)
print(f'numbers : {nums}')

numberRanking(nums)
