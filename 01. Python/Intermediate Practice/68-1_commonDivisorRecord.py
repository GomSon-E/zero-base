num1 = int(input('1보다 큰 정수 입력: '))
num2 = int(input('1보다 큰 정수 입력: '))

commonDivisorList = []

for i in range(1, num1 + 1):
    if num1 % i == 0 and num2 % i == 0:
        commonDivisorList.append(i)

with open('files/commonDivisorRecord.txt', 'a', encoding='utf-8') as f:
    f.write(f'{num1}와 {num2}의 공약수: {commonDivisorList}\n')

print('common divisor write complete!')