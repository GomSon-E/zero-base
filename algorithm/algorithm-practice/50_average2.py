subjects = ['국어 점수', '영어 점수', '수학 점수', '과학 점수', '국사 점수', '평균']
averageScoreList = [88, 82, 90, 78, 92, 86]
studentScoreList = [85, 90, 82, 88, 100]

totalStudentScore = 0
for s in studentScoreList:
    totalStudentScore += s
studentScoreList.append(totalStudentScore // 5)

exceptScoreList = []
for i in range(6):
    exceptScoreList.append(((averageScoreList[i] * 20 - studentScoreList[i]) / 19))

for i in range(6):
    deviation = round(studentScoreList[i] - exceptScoreList[i], 2)

    if deviation > 0:
        print(f'{subjects[i]} 차이: +{deviation}')
    else:
        print(f'{subjects[i]} 차이: {deviation}')

