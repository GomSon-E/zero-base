import random

userNums = [] ; randomNums = [] ; correctNums = [] ; bonusNum = 0

def setUserNums(num):
    global userNums
    userNums.append(num)

def getUserNums():
    return userNums

def setRandomNums():
    global randomNums
    randomNums = random.sample(range(1, 46), 6)

def getRandomNums():
    return randomNums

def setBonusNum():
    global bonusNum

    while True:
        num = random.randint(1, 46)

        if num not in randomNums:
            bonusNum = num
            break

def getBonusNum():
    return bonusNum

def getCorrectNums():
    global correctNums

    for num in userNums:
        if num in randomNums:
            correctNums.append(num)

    return correctNums

def getResult():
    correctCnt = len(getCorrectNums())

    if correctCnt == 6:
        print('!!1등 당첨!!')
        print(f'일치 번호: {correctNums}')
    elif correctCnt == 5:
        if bonusNum in userNums:
            print('!!2등 당첨!!')
            print(f'일치 번호: {correctNums}, 보너스 번호: {bonusNum}')
        else:
            print('!!3등 당첨!!')
            print(f'일치 번호: {correctNums}')
    elif correctCnt == 4:
        print('!!4등 당첨!!')
        print(f'일치 번호: {correctNums}')
    elif correctCnt == 3:
        print('!!5등 당첨!!')
        print(f'일치 번호: {correctNums}')
    else:
        print('아쉽습니다. 다음 기회에~')
        print(f'기계 번호:\t{randomNums}')
        print(f'보너스번호:\t{bonusNum}')
        print(f'선택 번호:\t{userNums}')
        print(f'일치 번호:\t{correctNums}')

def start():

    for i in range(6):
        num = int(input('번호(1~45) 입력: '))

        setUserNums(num)

    setRandomNums()
    setBonusNum()
    getResult()