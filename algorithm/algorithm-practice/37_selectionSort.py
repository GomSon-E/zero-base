def selectionSort(data, asc):
    for i in range(len(data) - 1):
        minValue = 0
        minIndex = 0

        if asc:
            for j in range(i, len(data)):
                if minValue == 0 or minValue > data[j]:
                    minValue = data[j]
                    minIndex = j
        else:
            for j in range(i, len(data)):
                if minValue == 0 or minValue < data[j]:
                    minValue = data[j]
                    minIndex = j

        data[i], data[minIndex] = data[minIndex], data[i]

    return data


nums = [6, 4, 13, 7, 9, 3, 8, 16, 19, 10]
print(f'not sorted nums : {nums}')
print(f'sorted nums by ASC : {selectionSort(nums, True)}')
print(f'sorted nums by DESC : {selectionSort(nums, False)}')