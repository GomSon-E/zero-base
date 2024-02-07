import random

order = ['가위', '바위', '보']

computer = random.randint(1, 3)
user = int(input('가위, 바위, 보 선택: 1. 가위\t2. 바위\t3. 보'))

if computer == user :
    print('무승부')
elif computer == 1 and user == 2 \
        or computer == 2 and user == 3 \
        or computer == 3 and user == 1 :
    print('컴퓨터: 패, 유저: 승')
else:
    print('컴퓨터: 승, 유저: 패')

print('컴퓨터: {}, 사용자: {}'.format(order[computer-1], order[user-1]))
