num = int(input('숫자 입력: '))

# 2진수
b = bin(num)
print(f'2진수: {b}')

# 8진수
o = oct(num)
print(f'8진수: {o}')

# 16진수
x = hex(num)
print(f'16진수: {x}')

# 2진수 -> 10진수
print(f'2진수\t->\t10진수: {b}\t->\t{int(b, 2)}')

# 8진수 -> 10진수
print(f'8진수\t->\t10진수: {o}\t\t->\t{int(o, 8)}')

# 16진수 -> 10진수
print(f'16진수\t->\t10진수: {x}\t\t->\t{int(x, 16)}')