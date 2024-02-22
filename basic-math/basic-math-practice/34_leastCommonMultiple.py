import random

num1 = random.randint(100, 1000)
num2 = random.randint(100, 1000)
print(f'[난수1] : {num1}')
print(f'[난수2] : {num2}')

gcd = 0
for i in range(1, num1 + 1):
    if num1 % i == 0 and num2 % i == 0:
        gcd = i

print(f'[최대공약수] : {gcd}')

lcm = (num1 * num2) // gcd
print(f'[최소공배수] : {lcm}')
