def findApproximation(data, value):
    nearValue = 0
    minDeviation = 0

    for d in data:
        deviation = abs(d - value)

        if minDeviation == 0 or minDeviation > deviation:
            minDeviation = deviation
            nearValue = d

    print(f'near bmi: {nearValue}')

    if nearValue == data[0]:
        print(f'user condition: 저체중')
    elif nearValue == data[1]:
        print(f'user condition: 정상')
    elif nearValue == data[2]:
        print(f'user condition: 과체중')


bmiData = [18.5, 23, 25]

weight = int(input('input weight(kg): '))
height = float(input('input height(m): '))

bmi = round(weight / height ** 2, 2)
print(f'user BMI: {bmi}')

findApproximation(bmiData, bmi)