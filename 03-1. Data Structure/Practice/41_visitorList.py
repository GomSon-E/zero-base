import random

# 영유아, 어린이, 청소년, 성인, 어르신
division = ['영유아', '어린이', '청소년', '성인', '어르신']
price = [0, 200, 300, 500, 0]
visitor = [0, 0, 0, 0, 0]
totalPrice = 0

for i in range(100):
    age = random.randint(0, 100)

    if 0 <= age <= 7:
        visitor[0] += 1
    elif 8 <= age <= 13:
        visitor[1] += 1
    elif 14 <= age <= 19:
        visitor[2] += 1
    elif 20 <= age <= 64:
        visitor[3] += 1
    else:
        visitor[4] += 1

print('-' * 30)

for i in range(5):
    totalPrice += price[i] * visitor[i]
    print(f'{division[i]}\t\t: {visitor[i]}명\t\t: {price[i] * visitor[i]}원')

print('-' * 30)
print(f'1일 요금 총합계: {totalPrice}원')
print('-' * 30)