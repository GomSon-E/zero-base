import time

def readTotal():
    with open('files/total.txt', 'r', encoding='utf-8') as f:
        return int(f.read())

def writeTotal(t):
    with open('files/total.txt', 'w', encoding='utf-8') as f:
        f.write(str(t))

def writeBook(w, c, m, t):
    with open('files/budgetBook.txt', 'a', encoding='utf-8') as f:
        f.write('-' * 30 + '\n')
        f.write(f'{time.strftime('%Y-%m-%D %H:%M:%S', time.localtime())}\n')
        f.write(f'[{w}] {c} : {m}원\n')
        f.write(f'[잔액] {t}원\n')


while True:
    choice = int(input('1. 입금\t2. 출금\t3. 종료'))

    if choice == 1:
        money = int(input('입금액 입력: '))
        content = input('입금 내역 입력: ')

        remain = readTotal()
        total = remain + money

        writeTotal(total)
        writeBook('입금', content, money, total)

        print('입금 완료!!')
        print(f'기존 잔액: {remain}')
        print(f'입금 후 잔액: {total}')

    elif choice == 2:
        money = int(input('출금액 입력: '))
        content = input('출금 내역 입력: ')

        remain = readTotal()
        total = remain - money

        writeTotal(total)
        writeBook('출금', content, money, total)

        print('출금 완료!!')
        print(f'기존 잔액: {remain}')
        print(f'출금 후 잔액: {total}')

    elif choice == 3:
        print('Bye~')
        break

    else:
        print('잘못된 입력값 입니다.')