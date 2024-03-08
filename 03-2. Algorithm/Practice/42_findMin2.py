scores = [100, 64, 94, 66, 75, 58, 99, 76, 96, 74, 54, 73, 88, 70, 68, 50, 95, 9, 69, 98]

total = 0
min = 0
for s in scores:
    total += s

    if min == 0 or min > s:
        min = s

average = total // len(scores)
print(f'평균 : {average}')
print(f'평균과 최솟값의 편차 : {min - average}')