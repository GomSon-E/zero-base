industry = int(input('업종 선택(1.가정용\t2.대중탕용\t3.공업용) : '))
usage = int(input('사용량 입력 : '))
cost = 0

if industry == 1 :
    cost = 540
elif industry == 2 :
    if usage <= 50 :
        cost = 820
    elif usage > 50 and usage <= 300 :
        cost = 1920
    else :
        cost = 2400
else :
    if usage <= 500 :
        cost = 240
    else :
        cost = 470

print('=' * 25)
print('상수도 요금표')
print('-' * 25)
print('사용량\t:\t요금')
print('{}\t\t:\t{}원'.format(usage, format(usage * cost, ',')))
