sn = 0
cnt = 0
denominator = 0
numerator = 0

i = 1
while sn < 100:
    denominator = i
    numerator = 1
    for j in range(1, i + 1):
        sn += (numerator / denominator)
        print(f'{numerator} / {denominator}', end=', ')

        if sn < 100:
            numerator += 1
            denominator -= 1
            cnt += 1

    i += 1
    print()

print(f'수열의 합이 최초로 100을 초과하는 {cnt}항의 값: {numerator} / {denominator}')
print(f'수열의 합이 최초로 100을 초과하는 {cnt}항까지의 합: {sn}')


