ranks = [9.12, 8.95, 8.12, 6.9, 6.18]

scores = [6.7, 5.9, 8.1, 7.9, 6.7, 7.3, 7.2, 8.2, 6.2, 5.8]

minScore = 0
maxScore = 0
totalScore = 0

for s in scores:
    totalScore += s

    if minScore == 0 or minScore > s:
        minScore = s

    if maxScore < s:
        maxScore = s

scores.remove(minScore)
scores.remove(maxScore)
totalScore -= minScore
totalScore -= maxScore

averageScore = round(totalScore / len(scores), 2)

for i in range(len(ranks) - 1):
    if ranks[i] > averageScore > ranks[i + 1]:
        ranks.insert(i + 1, averageScore)

for i in range(5):
    print(f'{i + 1}위 -> {ranks[i]}')


