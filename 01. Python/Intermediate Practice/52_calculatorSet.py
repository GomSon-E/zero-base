from arithmetic import basicOperator as bo
from arithmetic import developerOperator as do

from shape import triangleSquareArea as tsa
from shape import circleArea as ca

num1 = float(input('숫자1 입력: '))
num2 = float(input('숫자2 입력: '))

print(f'{num1} + {num2} = {bo.add(num1, num2)}')
print(f'{num1} + {num2} = {bo.subtract(num1, num2)}')
print(f'{num1} + {num2} = {bo.multiply(num1, num2)}')
print(f'{num1} + {num2} = {bo.divide(num1, num2)}')
print(f'{num1} + {num2} = {do.remainder(num1, num2)}')
print(f'{num1} + {num2} = {do.quotient(num1, num2)}')
print(f'{num1} + {num2} = {do.power(num1, num2)}')

width = float(input('가로 길이 입력: '))
height = float(input('세로 길이 입력: '))

print(f'삼각형 넓이: {tsa.triangleArea(width, height)}')
print(f'삼각형 넓이: {tsa.squareArea(width, height)}')

radius = float(input('반지름 입력: '))

print(f'원의 넓이: {ca.circleArea(radius)}')
