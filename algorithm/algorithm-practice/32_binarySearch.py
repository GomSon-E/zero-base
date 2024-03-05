def binarySearch(data, value):
    startIndex = 0
    endIndex = len(data) - 1
    midIndex = endIndex // 2
    midValue = data[midIndex]

    searchResult = -1

    while data[startIndex] <= midValue <= data[endIndex]:
        print(f'startIndex : {startIndex} ; endIndex : {endIndex}')
        print(f'midIndex : {midIndex} ; midValue : {midValue}')

        if midValue == value:
            searchResult = midIndex
            break

        elif midValue > value:
            endIndex = midIndex - 1

        elif midValue < value:
            startIndex = midIndex + 1

        midIndex = (endIndex + startIndex) // 2
        midValue = data[midIndex]

    print(f'numbers : {data}')
    print('>> search result <<')
    if searchResult == -1:
        print('!! search fail !!')
        print(f'search result index : {searchResult}')
    else:
        print('!! search success !!')
        print(f'search result index : {searchResult}')
        print(f'search result number : {data[searchResult]}')


nums = [1, 2, 4, 6, 7, 8, 10, 11, 13, 15, 16, 17, 20, 21, 23, 24, 27, 28]
num = int(input('input search number : '))
binarySearch(nums, num)