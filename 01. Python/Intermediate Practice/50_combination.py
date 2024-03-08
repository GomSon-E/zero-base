import combination as c

numN = int(input('numN 입력: '))
numR = int(input('numR 입력: '))

print(f'{numN}C{numR}: {c.getCombination(numN, numR, False)}')

listN = [1, 2, 3, 4, 5, 6, 7, 8]
numR = 3

c.getCombinations(listN, numR)