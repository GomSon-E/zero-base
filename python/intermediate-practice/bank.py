import random

class IntInputException(Exception):
    def __init__(self):
        super().__init__(f'입력값은 숫자여야 합니다.')

class WrongInputException(Exception):
    def __init__(self):
        super().__init__(f'잘못된 입력값 입니다.')

class InsufficientMoneyException(Exception):
    def __init__(self, total_money, money):
        super().__init__(f'잔고가 부족 합니다. 잔액: {total_money}, 출금액: {money}')

class BankAccount:
    def __init__(self, name, no, total_money):
        self.name = name
        self.no = no
        self.totalMoney = total_money

    def printBankAccountInfo(self):
        print('-' * 30)
        print(f'Account Name: {self.name}')
        print(f'Account No: {self.no}')
        print(f'Total Money: {self.totalMoney}')

    def deposit(self):
        money = input('입금액 입력: ')

        if money.isdigit():
            money = int(money)
        else:
            raise IntInputException

        self.totalMoney += money

    def withdraw(self):
        money = input('출금액 입력: ')

        if money.isdigit():
            money = int(money)
        else:
            raise IntInputException

        if money > self.totalMoney:
            raise InsufficientMoneyException(self.totalMoney, money)
        else:
            self.totalMoney -= money

def openBankAccount():
    name = input('통장 개설을 위한 예금주 입력: ')
    no = format(random.randint(0, 99999), '05d')
    total_money = 0
    account = BankAccount(name, no, total_money)
    account.printBankAccountInfo()
    return account





