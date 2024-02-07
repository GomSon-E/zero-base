number = int(input('정수 입력 : '))

sum = 0
oddSum = 0
evenSum = 0
factorial = 1;

for i in range(1, number + 1) :
    sum += i
    factorial *= i

    if i % 2 != 0:
        oddSum += i
    else :
        evenSum += i

print('합 결과 :', sum)
print('홀수 합 결과 :', oddSum)
print('짝수 합 결과 :', evenSum)
print('팩토리얼 결과 :', format(factorial, ','))
