age = int(input('나이 입력 : '))
week = ['금', '월', '화', '수', '목', '금', '월', '화', '수', '목']

if age <= 19 or age >= 65 :
    endOfYear = int(input('출생 연도 끝자리 입력 : '))
    print('{}요일 접종 가능!!'.format(week[endOfYear]))
else :
    print('하반기 일정 확인')
