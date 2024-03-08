messageLength = len(input('메시지 입력 : '))
if messageLength <= 50 :
    print('SMS 발송!!')
    print('메시지 길이 :', messageLength)
    print('메시지 발송 요금: 50원')
else :
    print('MMS 발송!!')
    print('메시지 길이 :', messageLength)
    print('메시지 발송 요금: 100원')