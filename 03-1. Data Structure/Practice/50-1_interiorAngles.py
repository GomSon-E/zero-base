dic = {}

for i in range(3, 11):
    angleSum = 180 * (i - 2)
    angle = int(angleSum / i)
    dic[i] = [angleSum, angle]

print(dic)