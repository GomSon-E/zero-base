principal = int(input('금액 입력 : '))
interest = float(input('이율 입력 : '))
duration = int(input('기간 입력 : '))
fv = principal * (1 + interest / 100) ** duration

print('-' * 20)
print('이율: {}%'.format(interest))
print('원금: {}원'.format(format(principal, ',')))
print('{}년 후 금액: {}원'.format(duration, format(int(fv), ',')))
print('-' * 20)