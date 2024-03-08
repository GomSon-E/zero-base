import discountRate

priceList = []

while True:
    choice = int(input('상품을 구매 하시겠어요? 1. 구매\t2. 종료'))

    if choice == 2:
        result = discountRate.get(priceList)
        print(f'할인율: {result[0]}')
        print(f'합계: {format(result[1], ',')}원')
        break

    price = int(input('상품 가격 입력: '))
    priceList.append(price)
