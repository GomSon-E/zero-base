def add(a, b):
    print(f'{a} + {b} = {a + b}')

def subtract(a, b):
    print(f'{a} - {b} = {a - b}')

def multiply(a, b):
    print(f'{a} * {b} = {a * b}')

def divide(a, b):
    print(f'{a} / {b} = {a / b}')

def remainder(a, b):
    print(f'{a} % {b} = {a % b}')

def quotient(a, b):
    print(f'{a} // {b} = {a // b}')

def power(a, b):
    print(f'{a} ** {b} = {a ** b}')


while True:
    print('-' * 100)

    choice = int(input('1. 덧셈\t2. 뺄셈\t3. 곱셈\t4. 나눗셈\t5. 나머지\t6. 몫\t7. 제곱승\t8. 종료'))

    if choice == 8:
        print('Bye~')
        break

    num1 = float(input('첫 번째 숫자 입력 : '))
    num2 = float(input('두 번째 숫자 입력 : '))

    if choice == 1:
        add(num1, num2)
    elif choice == 2:
        subtract(num1, num2)
    elif choice == 3:
        multiply(num1, num2)
    elif choice == 4:
        divide(num1, num2)
    elif choice == 5:
        remainder(num1, num2)
    elif choice == 6:
        quotient(num1, num2)
    elif choice == 7:
        power(num1, num2)

    print('-' * 100)