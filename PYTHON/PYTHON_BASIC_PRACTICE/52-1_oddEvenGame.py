import random

computer = random.randint(1, 2)
user = int(input('홀/짝 선택 : 1. 홀\t2. 짝'))

if computer == user and computer == 1 :
    print('빙고!! 홀수!!!')
elif computer == user and computer == 2 :
    print('빙고!! 짝수!!!')
elif computer != user and computer == 1 :
    print('실패!! 홀수!!!')
elif computer != user and computer == 2 :
    print('실패!! 짝수!!!')
