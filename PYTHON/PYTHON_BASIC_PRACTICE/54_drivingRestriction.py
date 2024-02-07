import datetime

fineDust = int(input('미세먼지 수치 입력 : '))
vehicleType = int(input('차량 종류 선택. 1.승용차\t2.영업용차'))
vehicleNumber = int(input('차량 번호 입력 : '))
endNumber = vehicleNumber % 10

now = datetime.datetime.now()

print('-' * 25)
print(now)
print('-' * 25)

if fineDust <= 150 or vehicleType == 2 :
    if endNumber == now.weekday() + 1 or endNumber == now.weekday() + 6 :
        print('금일 운행이 가능합니다!')
    else :
        print('차량 5부제 적용')
        print('차량 5부제로 금일 운행제한 대상 차량입니다.')
else :
    if (now.day % 2) == (endNumber % 2) :
        print('금일 운행이 가능합니다!')
    else :
        print('차량 2부제 적용')
        print('차량 2부제로 금일 운행제한 대상 차량입니다.')

print('-' * 25)
