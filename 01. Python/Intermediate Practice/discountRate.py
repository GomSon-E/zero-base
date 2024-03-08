def get(priceList):
    length = len(priceList)

    if length == 0:
        print('구매 상품이 없습니다.')
        return

    if length >= 5:
        rate = 25
    else:
        rate = length * 5

    total = int(sum(priceList) - (sum(priceList) * rate / 100))

    return [rate, total]
