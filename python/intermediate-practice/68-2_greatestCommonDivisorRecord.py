import math

num1 = int(input('1보다 큰 정수 입력: '))
num2 = int(input('1보다 큰 정수 입력: '))

with open('files/greatestCommonDivisorRecord.txt', 'a', encoding='utf-8') as f:
    f.write(f'{num1}와 {num2}의 최대공약수: {math.gcd(num1, num2)}\n')

print('greatest common divisor write complete!')