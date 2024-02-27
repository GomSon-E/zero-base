dic = {}

for i in range(2, 11):
    divisor = []
    for j in range(1, i + 1):
        if i % j == 0:
            divisor.append(j)

    dic[i] = divisor

print(dic)