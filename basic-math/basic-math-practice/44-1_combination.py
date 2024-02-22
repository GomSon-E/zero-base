n = int(input('numN 입력: '))
p = int(input('numP 입력: '))

result = 1
for i in range(p):
    result *= (n / p)
    n -= 1
    p -= 1

print(int(result))
