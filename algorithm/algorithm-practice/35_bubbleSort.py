def bubbleSort(data, asc):
    for i, n1 in enumerate(data):
        for j, n2 in enumerate(data):
            if asc:
                if n1 < n2:
                    data[i], data[j] = data[j], data[i]
            else:
                if n1 > n2:
                    data[i], data[j] = data[j], data[i]
    return data


nums = [10, 4, 1, 13, 16, 19, 14, 6, 5]
print(f'not sorted nums : {nums}')
print(f'sorted nums by ASC : {bubbleSort(nums, True)}')
print(f'sorted nums by DESC : {bubbleSort(nums, False)}')


