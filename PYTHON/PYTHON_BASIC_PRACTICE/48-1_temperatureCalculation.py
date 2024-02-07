altitude = int(input('고도 입력 : '))
temperature = 29 - (altitude // 60 * 0.8)

if altitude % 60 != 0 :
    temperature -= 0.8

print('지면 온도: 29')
print('고도 {}m의 기온: {}'.format(altitude, temperature))