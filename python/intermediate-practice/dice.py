import random

class Dice:
    def __init__(self):
        self.computer = 0
        self.user = 0

    def setComputer(self):
        print('[Dice] setComputer()')
        self.computer = random.randint(1, 6)

    def setUser(self):
        print('[Dice] setUser()')
        self.user = random.randint(1, 6)

    def startGame(self):
        print('[Dice] startGame()')
        self.setComputer()
        self.setUser()

    def printResult(self):
        print('[Dice] printResult()')
        print(f'컴퓨터 vs 유저 : {self.computer} vs {self.user} >> ', end='')
        if self.computer > self.user:
            print('컴퓨터 승!!')
        elif self.user > self.computer:
            print('유저 승!!')
        else:
            print('무승부!!')