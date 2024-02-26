n = int(input('1보다 큰 정수 입력: '))

divisorList = []
primeList = []

# 약수
for i in range(1, n+1):
    if n % i == 0:
        divisorList.append(i)

print(f'{n}의 약수: {divisorList}')

# 소수
for i in range(2, n+1):
    isPrime = True

    for j in range(2, i):
        if i % j == 0:
            isPrime = False
            break

    if isPrime:
        primeList.append(i)

print(f'{n}까지의 소수: {primeList}')