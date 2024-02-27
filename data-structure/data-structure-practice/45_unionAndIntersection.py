tuple1 = (1, 3, 2, 6, 12, 5, 7, 8)
tuple2 = (0, 5, 2, 9, 8, 6, 17, 3)

union = []
intersection = []

for i in tuple1:
    if i not in union:
        union.append(i)

for i in tuple2:
    if i not in union:
        union.append(i)

    if i in tuple1:
        intersection.append(i)

print(f'합집합(중복): {tuple(sorted(union))}')
print(f'교집합: {tuple(sorted(intersection))}')