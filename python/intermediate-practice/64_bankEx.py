import bank

myAccount = bank.openBankAccount()

while True:
    print('-' * 30)
    choice = input('1. 입금,\t2. 출금,\t3. 종료')

    if choice.isdigit():
        choice = int(choice)
    else:
        raise bank.IntInputException

    if choice == 1:
        try:
            myAccount.deposit()
        except Exception as e:
            print(e)
        finally:
            myAccount.printBankAccountInfo()

    elif choice == 2:
        try:
            myAccount.withdraw()
        except Exception as e:
            print(e)
        finally:
            myAccount.printBankAccountInfo()

    elif choice == 3:
        print('Bye~')
        break

    else:
        raise bank.WrongInputException