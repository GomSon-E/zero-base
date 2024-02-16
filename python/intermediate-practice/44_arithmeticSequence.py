def arithmeticSequence(a1, d, n):
    sum = 0

    for i in range(1, n+1):
        a = d * (i - 1) + a1
        sum += a
        print(f'{i}번째 항의 값: {a}')
        print(f'{i}번째 항까지의 값: {sum}')


a1 = int(input('a1 입력: '))
d = int(input('공차 입력: '))
n = int(input('n 입력: '))

arithmeticSequence(a1, d, n)
