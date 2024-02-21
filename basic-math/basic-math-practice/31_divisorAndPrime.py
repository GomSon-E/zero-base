import random

n = random.randint(100, 1000)
print(f'[난수] : {n}')

for i in range(1, n + 1):

    if i == 1:
        print(f'[약수] : 1')
        continue

    # 약수
    divisor = False

    if n % i == 0:
        divisor = True

    # 소수
    prime = True

    for j in range(2, i):
        if i % j == 0:
            prime = False
            break

    if divisor and prime:
        print(f'[소인수] : {i}')
    elif divisor:
        print(f'[약수] : {i}')
    elif prime:
        print(f'[소수] : {i}')