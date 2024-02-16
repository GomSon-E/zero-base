hour = int(input('시간 입력 : '))
minute = int(input('분 입력 : '))
second = int(input('초 입력 : '))

totalSecond = hour * 60 ** 2 + minute * 60 + second

print('{}초'.format(format(totalSecond, ',')))