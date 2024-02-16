age = input('나이 입력 : ')

if age.isdigit() :
    age = int(age)
    print('{}년({}년후)에 100살!!'.format((100 - age + 2024), (100 - age)))
else :
    print('잘 못 입력했습니다.')
