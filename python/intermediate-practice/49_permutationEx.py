import permutation as p

numN = int(input('numN 입력: '))
numR = int(input('numR 입력: '))

print(f'{numN}P{numR}: {p.getPermutation(numN, numR, False)}')

listN = [1, 2, 3, 4, 5, 6, 7, 8]
numR = 3

p.getPermutations(listN, numR)