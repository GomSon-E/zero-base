n = int(input('n 입력: '))

an = 2
bn = 3 # 3, 6, 9, ...

for i in range(n):
    print(f'{i}번째 항: {an}')
    an += bn
    bn += 3