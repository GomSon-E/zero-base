n = int(input('numN 입력: '))
p = int(input('numP 입력: '))

result = 1

for i in range(n, (n - p), -1):
    result *= i
    print(f'n : {i}')

print(f'result : {result}')
