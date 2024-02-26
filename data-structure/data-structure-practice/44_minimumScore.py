scores = ((3.7, 4.2), (2.9, 4.3), (4.1, 4.2))

total = 0
average = 0

for i, j in scores:
    total += i + j

print(f'3학년 총학점: {total}')
print(f'3학년 평균: {total / 6}')
print('-' * 30)
goalScore = round(4 * 8 - total, 1)
print(f'4학년 목표 학점: {goalScore}')
minimumScore = goalScore / 2
print(f'4학년 한학기 최소학점: {minimumScore}')
print('-' * 30)
scores = list(scores)
scores.append((minimumScore, minimumScore))
print(f'scores: {tuple(scores)}')