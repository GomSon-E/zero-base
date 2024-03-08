childPrice = 18000
infantPrice = 25000
adultPrice = 50000
discountRate = 0.5

def receiptPrinter(c1, c2, i1, i2, a1, a2):
    print('=' * 45)

    cp = childPrice * c1
    print(f'유아 {c1}명 요금 : {format(cp, ',')}원')

    cdp = int(childPrice * discountRate * c2)
    print(f'유아 할인 대상 {c2}명 요금 : {format(cdp, ',')}원')

    ip = infantPrice * i1
    print(f'소아 {i1}명 요금 : {format(ip, ',')}원')

    idp = int(infantPrice * discountRate * i2)
    print(f'소아 할인 대상 {i2}명 요금 : {format(idp, ',')}원')

    ap = adultPrice * a1
    print(f'성인 {a1}명 요금 : {format(ap, ',')}원')

    adp = int(adultPrice * discountRate * a2)
    print(f'성인 할인 대상 {a2}명 요금 : {format(adp, ',')}원')

    print('=' * 45)

    print(f'Total: {c1 + c2 + i1 + i2 + a1 + a2}명')
    print(f'Total Price : {format(cp + cdp + ip + idp + ap + adp, ',')}원')

    print('=' * 45)


childCnt = int(input('유아 입력: '))
childDiscountCnt = int(input('할인 대상 유아 입력: '))
infantCnt = int(input('소아 입력: '))
infantDiscountCnt = int(input('할인 대상 소아 입력: '))
adultCnt = int(input('성인 입력: '))
adultDiscountCnt = int(input('할인 대상 성인 입력: '))

receiptPrinter(childCnt, childDiscountCnt, infantCnt, infantDiscountCnt, adultCnt, adultDiscountCnt)
