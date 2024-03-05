def insertionSort(arr, asc):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1

        if asc:
            while j >= 0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        else:
            while j >= 0 and key > arr[j] :
                arr[j+1] = arr[j]
                j -= 1

        arr[j+1] = key

        print(f'nums : {nums}')

    return arr


nums = [19, 10, 3, 5, 13, 4, 12, 17, 8, 16]
print(f'not sorted nums : {nums}')
print(f'sorted nums by ASC : {insertionSort(nums, True)}')
print(f'sorted nums by DESC : {insertionSort(nums, False)}')