import random

target = random.randint(1, 1001)
cnt = 0

while True :
    cnt += 1
    userNumber = int(input('1에서 1000까지의 정수 입력 : '))

    if target == userNumber :
        print('빙고!')
        print('난수 : {}, 시도 횟수 : {}'.format(target, cnt))
        break
    elif target > userNumber :
        print('난수가 크다!')
    else :
        print('난수가 작다!')