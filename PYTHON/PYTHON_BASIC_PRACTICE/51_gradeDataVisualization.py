koreanA = 85
englishA = 82
mathA = 89
scienceA = 75
historyA = 94

koreanS = int(input('국어 점수 입력 : '))
englishS = int(input('영어 점수 입력 : '))
mathS = int(input('수학 점수 입력 : '))
scienceS = int(input('과학 점수 입력 : '))
historyS = int(input('국사 점수 입력 : '))

koreanD = koreanS - koreanA
englishD = englishS - englishA
mathD = mathS - mathA
scienceD = scienceS - scienceA
historyD = historyS - historyA

totalS = koreanS + englishS + mathS + scienceS + historyS
averageS = totalS // 5

totalD = koreanD + englishD + mathD + scienceD + historyD
averageD = totalD // 5

print('-' * 100)
print('총점: {}({}), 평균: {}({})'.format(totalS, totalD, averageS, averageD))
print('국어: {}({})'.format(koreanS, koreanD), end=' ')
print('영어: {}({})'.format(englishS, englishD), end=' ')
print('수학: {}({})'.format(mathS, mathD), end=' ')
print('과학: {}({})'.format(scienceS, scienceD), end=' ')
print('국사: {}({})'.format(historyS, historyD), )
print('-' * 100)
print('국어 편차: {}({})'.format(('+' * (koreanD if koreanD > 0 else -koreanD)), koreanD))
print('영어 편차: {}({})'.format(('+' * (englishD if englishD > 0 else -englishD)), englishD))
print('수학 편차: {}({})'.format(('+' * (mathD if mathD > 0 else -mathD)), mathD))
print('과학 편차: {}({})'.format(('+' * (scienceD if scienceD > 0 else -scienceD)), scienceD))
print('국사 편차: {}({})'.format(('+' * (historyD if historyD > 0 else -historyD)), historyD))
print('총점 편차: {}({})'.format(('+' * (totalD if totalD > 0 else -totalD)), totalD))
print('평균 편차: {}({})'.format(('+' * (averageD if averageD > 0 else -averageD)), averageD))
print('-' * 100)

