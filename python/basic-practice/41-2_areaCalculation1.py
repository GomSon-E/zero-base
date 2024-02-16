width = float(input('가로 길이 입력: '))
height = float(input('세로 길이 입력: '))

print('-' * 10, 'Result', '-' * 10)
print('삼각형 넓이 : %.6f' % (width * height / 2))
print('사각형 넓이 : %.6f' % (width * height))
print('삼각형 넓이 : %.2f' % (width * height / 2))
print('시각형 넓이 : %.2f' % (width * height))
print('-' * 25)