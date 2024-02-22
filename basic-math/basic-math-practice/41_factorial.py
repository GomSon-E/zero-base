num = int(input('n 입력: '))

# for문 이용
def factorial1(n):
    result = 1
    for i in range(1, n+1):
        result *= i

    return result

# 재귀함수 이용
def factorial2(n):
    if n == 1:
        return 1
    else:
        return n * factorial2(n-1)

# 모듈 이용
def factorial3(n):
    import math

    return math.factorial(n)


print(factorial1(num))
print(factorial2(num))
print(factorial3(num))