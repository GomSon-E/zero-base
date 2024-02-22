import random

num1 = random.randint(100, 1000)
num2 = random.randint(100, 1000)
print(f'[난수1] : {num1}')
print(f'[난수2] : {num2}')

cdList = []

for i in range(1, (num1 if num1 > num2 else num2) + 1):
    if num1 % i == 0 and num2 % i == 0:
        cdList.append(i)

print(f'공약수: {cdList}')
print(f'최대공약수: {max(cdList)}')