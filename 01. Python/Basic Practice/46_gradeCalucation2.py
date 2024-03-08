koreanScore = int(input('국어 점수 입력: '))
englishScore = int(input('영어 점수 입력: '))
mathScore = int(input('수학 점수 입력: '))

totalScore = koreanScore + englishScore + mathScore
averageScore = totalScore / 3

print('총점: ', totalScore)
print('평균: %.2f' % averageScore)
print('-' * 20)

minScore = min(koreanScore, englishScore, mathScore)
minSubject = ''
if minScore == koreanScore :
    minSubject = '국어'
elif minScore == englishScore :
    minSubject = '영어'
else :
    minSubject = '수학'

maxScore = max(koreanScore, englishScore, mathScore)
maxSubject = ''
if maxScore == koreanScore :
    maxSubject = '국어'
elif maxScore == englishScore :
    maxSubject = '영어'
else :
    maxSubject = '수학'

print('최고 점수 과목(점수): {}({})'.format(maxSubject, maxScore))
print('최저 점수 과목(점수): {}({})'.format(minSubject, minScore))
print('최고, 최저 점수 차이: ', (maxScore - minScore))
print('-' * 20)
