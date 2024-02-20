def getPermutation(n, r, logPrint=True):
    result = 1
    for i in range(n, (n - r), -1):
        if logPrint:
            print(f'n: {i}')
        result *= i

    return result


from itertools import permutations

def getPermutations(nList, r):
    pList = list(permutations(nList, r))
    print(f'{len(nList)}P{r} 개수: {len(pList)}')

    for i in pList:
        print(i, end=', ')
