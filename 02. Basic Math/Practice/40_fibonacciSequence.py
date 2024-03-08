n = int(input('n 입력: '))

an = 1
sn = 0

prev1 = 1
prev2 = 1

for i in range(1, n + 1):
    if i == 1 or i == 2:
        sn += an
    else:
        an = prev1 + prev2
        sn += an
        prev2 = prev1
        prev1 = an

    print(f'{i}번째 항: {an}')
    print(f'{i}번째까지의 합: {sn}')