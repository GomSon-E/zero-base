customerName = input('고객명 : ')
productName = input('상품명 : ')
orderNumber = input('주문번호 : ')
payMethod = input('결재방법 : ')
productPrice = int(input('상품금액 : '))
payPrice = int(input('결재금액 : '))
point = int(input('포인트 : '))
payDate = input('결제일시 : ')
installmentMonth = int(input('할부 개월 수 : '))
installmentType = input('할부유형 : ')

print('{} 고객님 안녕하세요.'.format(customerName))
print('{} 고객님의 주문이 완료되었습니다.'.format(customerName))
print('다음은 주문건에 대한 상세 내역입니다.')
print('-' * 20)
print('상품명\t: {}'.format(productName))
print('주문번호\t: {}'.format(orderNumber))
print('결재방법\t: {}'.format(payMethod))
print('상품금액\t: {} 원'.format(productPrice))
print('결재금액\t: {} 원'.format(payPrice))
print('포인트\t: {} P'.format(point))
print('결제일시\t: {}'.format(payDate))
print('할부\t\t: {} 개월'.format(installmentMonth))
print('할부유형\t: {}'.format(productName))
print('문의\t\t: 010-1234-5678')
print('-' * 20)
print('저희 사이트를 이용해 주셔서 감사합니다.')

