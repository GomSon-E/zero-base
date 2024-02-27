fruits = ({'수박': 8}, {'포도': 13}, {'참외': 12}, {'사과': 17}, {'자두': 19}, {'자몽': 15})
fruits = list(fruits)

currentIndex = 0
nextIndex = 0
totalIndex = len(fruits) - 1

while True:
    nextIndex += 1

    currentItem = fruits[currentIndex]
    nextItem = fruits[nextIndex]

    if list(currentItem.values())[0] > list(nextItem.values())[0]:
        fruits.insert(nextIndex, fruits.pop(currentIndex))

    if nextIndex >= totalIndex:
        nextIndex = currentIndex
        currentIndex += 1

    if currentIndex > totalIndex:
        break

print(f'오름차순 정렬: {tuple(fruits)}')
fruits.reverse()
print(f'내림차순 정렬: {tuple(fruits)}')

