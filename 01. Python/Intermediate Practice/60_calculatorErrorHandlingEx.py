import calculatorErrorHandling as e

num1 = input('첫번째 값 입력: ')
num2 = input('두번째 값 입력: ')

print('덧셈 연산')
e.add(num1, num2)

print('뺄셈 연산')
e.sub(num1, num2)

print('곱셈 연산')
e.mul(num1, num2)

print('나눗셈 연산')
e.div(num1, num2)

print('나머지 연산')
e.mod(num1, num2)

print('몫 연산')
e.flo(num1, num2)

print('거듭제곱 연산')
e.exp(num1, num2)