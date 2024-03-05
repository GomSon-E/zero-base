def findApproximation(data, value):
    nearValue = 0
    minDeviation = 0

    for key in data:
        deviation = abs(key - value)

        if minDeviation == 0 or minDeviation > deviation:
            minDeviation = deviation
            nearValue = key

    print(f'depth: {value}m')
    print(f'water temperature: {data[nearValue]}도')


waterInfo = {0: 24, 5: 22, 10: 20, 15: 16, 20: 13, 25: 10, 30: 6}
num = int(input('input depth: '))
findApproximation(waterInfo, num)