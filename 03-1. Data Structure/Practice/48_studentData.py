studentCnt = ({'cls01': 18},
              {'cls02': 21},
              {'cls03': 20},
              {'cls04': 19},
              {'cls05': 22},
              {'cls06': 20},
              {'cls07': 23},
              {'cls08': 17})

totalCnt = 0 ; averageCnt = 0 ; minCls = {'zero': 0} ; maxCls = {'zero': 0}
cntDeviation = []

for i in studentCnt:
    value = list(i.values())[0]

    totalCnt += value

    minCnt = list(minCls.values())[0]
    if minCnt > value or minCnt == 0:
        minCls = i

    if list(maxCls.values())[0] < value:
        maxCls = i

averageCnt = totalCnt / len(studentCnt)

for i in studentCnt:
    key = list(i.keys())[0]
    value = list(i.values())[0]
    deviation = value - averageCnt
    cntDeviation.append({key: deviation})

print(f'전체 학생 수: {totalCnt}명')
print(f'평균 학생 수: {averageCnt}명')
print(f'학생 수가 가장 적은 학급: {list(minCls.keys())[0]}({list(minCls.values())[0]}명)')
print(f'학생 수가 가장 많은 학급: {list(maxCls.keys())[0]}({list(maxCls.values())[0]}명)')
print(f'학급별 학생 편차: {tuple(cntDeviation)}')
