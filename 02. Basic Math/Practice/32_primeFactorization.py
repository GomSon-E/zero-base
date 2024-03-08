import random

num = random.randint(100, 1000)
print(f'[난수] : {num}')

i = 2
primeDic = {}
while i <= num:
    if num % i == 0:
        if i in primeDic.keys():
            primeDic[i] += 1
        else:
            primeDic[i] = 1

        num /= i
    else:
        i += 1

print(f'소인수: {list(primeDic.keys())}')

for i in primeDic.keys():
    print(f'{i}의 지수: {primeDic[i]}')