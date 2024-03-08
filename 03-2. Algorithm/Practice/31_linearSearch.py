def linearSearch(data, value):
    index = -1

    for d in data:
        index += 1
        if d == value:
            break

    print(f'numbers : {data}')
    print(f'search number : {value}')

    if index == -1:
        print('!! search fail !!')
        print('>> search result <<')
        print(f'search result index : {index}')
    else:
        print('!! search success !!')
        print('>> search result <<')
        print(f'search result index : {index}')
        print(f'search result value : {data[index]}')


import random

nums = random.sample(range(1, 21), 10)
num = int(input('찾으려는 숫자 입력 : '))
linearSearch(nums, num)