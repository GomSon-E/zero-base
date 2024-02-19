def add(a, b):
    try:
        a = float(a)
    except:
        print('첫번째 값이 숫자가 아닙니다.')
        return

    try:
        b = float(b)
    except:
        print('두번째 값이 숫자가 아닙니다.')
        return

    print(f'{a} + {b} = {a + b}')

def sub(a, b):
    try:
        a = float(a)
    except:
        print('첫번째 값이 숫자가 아닙니다.')
        return

    try:
        b = float(b)
    except:
        print('두번째 값이 숫자가 아닙니다.')
        return

    print(f'{a} - {b} = {a - b}')

def mul(a, b):
    try:
        a = float(a)
    except:
        print('첫번째 값이 숫자가 아닙니다.')
        return

    try:
        b = float(b)
    except:
        print('두번째 값이 숫자가 아닙니다.')
        return

    print(f'{a} * {b} = {a * b}')

def div(a, b):
    try:
        a = float(a)
    except:
        print('첫번째 값이 숫자가 아닙니다.')
        return

    try:
        b = float(b)
    except:
        print('두번째 값이 숫자가 아닙니다.')
        return

    try:
        result = a / b
    except:
        print('0으로 나눌 수 없습니다.')
        return

    print(f'{a} / {b} = {result}')


def mod(a, b):
    try:
        a = float(a)
    except:
        print('첫번째 값이 숫자가 아닙니다.')
        return

    try:
        b = float(b)
    except:
        print('두번째 값이 숫자가 아닙니다.')
        return

    try:
        result = a % b
    except:
        print('0으로 나눌 수 없습니다.')
        return

    print(f'{a} % {b} = {result}')

def flo(a, b):
    try:
        a = float(a)
    except:
        print('첫번째 값이 숫자가 아닙니다.')
        return

    try:
        b = float(b)
    except:
        print('두번째 값이 숫자가 아닙니다.')
        return

    try:
        result = a // b
    except:
        print('0으로 나눌 수 없습니다.')
        return

    print(f'{a} // {b} = {result}')

def exp(a, b):
    try:
        a = float(a)
    except:
        print('첫번째 값이 숫자가 아닙니다.')
        return

    try:
        b = float(b)
    except:
        print('두번째 값이 숫자가 아닙니다.')
        return

    print(f'{a} ** {b} = {a ** b}')
