midterm = input('중간 고사 점수: ')
final = input('기말 고사 점수: ')

if midterm.isdigit() and final.isdigit():
    midterm = int(midterm)
    final = int(final)
    print('총점: {}, 평균: {}'.format((midterm + final), ((midterm + final) / 2)))

else :
    print('잘 못 입력했습니다.')
