price = int(input('상품 가격 입력 : '))
pay = int(input('지불 금액 : '))
change = int((pay - price) / 10) * 10

print('거스름 돈 : {}(원단위 절사)'.format(change))
print('-' * 20)

num50000 = change // 50000
print('50,000 {}장'.format(num50000))
change -= 50000 * num50000

num10000 = change // 10000
print('10,000 {}장'.format(num10000))
change -= 10000 * num10000

num5000 = change // 5000
print('5,000 {}장'.format(num5000))
change -= 5000 * num5000

num1000 = change // 1000
print('1000 {}장'.format(num1000))
change -= 1000 * num1000

num500 = change // 500
print('500 {}개'.format(num500))
change -= 500 * num500

num100 = change // 100
print('100 {}개'.format(num100))
change -= 100 * num100

num10 = change // 10
print('10 {}개'.format(num10))

print('-' * 20)