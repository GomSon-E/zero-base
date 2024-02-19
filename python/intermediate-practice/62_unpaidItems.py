prices = [1200, 1000, 800, 2000, 900]
totalCost = 0
unpaidItems = {}

for i in range(5):
    goods = input(f'goods{i + 1} 구매 개수: ')

    try:
        goods = int(goods)
    except Exception as e:
        print(e)
        key = 'goods' + str(i)
        unpaidItems[key] = goods
    else:
        totalCost += prices[i] * goods

print('-' * 45)
print(f'총 구매 금액: {format(totalCost, ',')}원')
print('-' * 45)
print('-' * 17, '미결제 항목', '-' * 17)
print(unpaidItems)
for k in unpaidItems.keys():
    print(f'상품: {k}\t\t구매 개수: {unpaidItems[k]}')
print('-' * 45)