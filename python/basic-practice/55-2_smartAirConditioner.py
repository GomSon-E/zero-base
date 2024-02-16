temperature = int(input('실내 온도 입력 : '))

if temperature <= 18 :
    print('에어컨: OFF!!')
elif 18 < temperature <= 22 :
    print('에어컨 : 매우 약!!')
elif 22 < temperature <= 24 :
    print('에어컨 : 약!!')
elif 24 < temperature <= 26 :
    print('에어컨 : 중!!')
elif 26 < temperature <= 28 :
    print('에어컨 : 강!!')
else :
    print('에어컨 : 매우 강!!')
