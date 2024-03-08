def geometricSequence(a1, r, n):
    sum = 0

    for i in range(1, n+1):
        a = a1 * (r ** (i - 1))
        sum += a
        print(f'{i}번째 항의 값: {a}')
        print(f'{i}번째 항까지의 값: {sum}')


a1 = int(input('a1 입력: '))
r = int(input('공비 입력: '))
n = int(input('n 입력: '))

geometricSequence(a1, r, n)