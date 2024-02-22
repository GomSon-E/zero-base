n = int(input('n 입력: '))
an = 4 + (n - 1) * 6
sn = int(n * (4 + an) / 2)
print(f'n번째 항의 값: {an}')
print(f'n번째 항까지의 값: {sn}')