def getCombination(n, r, logPrint=True):
    resultP = 1
    resultR = 1

    for i in range(n, (n - r), -1):
        resultP *= i

    for i in range(1, r + 1):
        resultR *= i

    resultC = int(resultP / resultR)

    if logPrint:
        print(f'resultP : {resultP}')
        print(f'resultR : {resultR}')
        print(f'resultC : {resultC}')

    return resultC

from itertools import combinations

def getCombinations(nList, r):
    cList = list(combinations(nList, r))
    print(f'{len(nList)}C{r} 개수: {len(cList)}')

    for i in cList:
        print(i, end=', ')