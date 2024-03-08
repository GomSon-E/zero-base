def mergeSort(data, asc):

    if len(data) < 2:
        return data

    midIndex = len(data) // 2

    leftNums = mergeSort(data[:midIndex], asc)
    rightNums = mergeSort(data[midIndex:], asc)

    mergeNums = []
    leftIndex = 0
    rightIndex = 0

    while leftIndex < len(leftNums) and rightIndex < len(rightNums) :
        if asc:
            if leftNums[leftIndex] < rightNums[rightIndex]:
                mergeNums.append(leftNums[leftIndex])
                leftIndex += 1
            else:
                mergeNums.append(rightNums[rightIndex])
                rightIndex += 1
        else:
            if leftNums[leftIndex] > rightNums[rightIndex]:
                mergeNums.append(leftNums[leftIndex])
                leftIndex += 1
            else:
                mergeNums.append(rightNums[rightIndex])
                rightIndex += 1

    mergeNums = mergeNums + leftNums[leftIndex:]
    mergeNums = mergeNums + rightNums[rightIndex:]

    print(f'nums : {mergeNums}')
    return mergeNums


nums = [24, 62, 81, 28, 51, 10, 85, 76, 71, 91, 54, 56, 94, 49, 25, 28, 88, 50, 41, 84]
print(f'not sorted nums : {nums}')
print(f'sorted nums by ASC : {mergeSort(nums, True)}')
print(f'sorted nums by DESC : {mergeSort(nums, False)}')

