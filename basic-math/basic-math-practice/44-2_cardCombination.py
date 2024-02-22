def getPossibility(n, p):
    result = 1

    for i in range(p):
        result *= (n / p)
        n -= 1
        p -= 1

    return 1 / int(result) * 100


print(f'카드 7장 중 3장을 선택했을 때, 3, 4,5가 동시에 선택될 수 있는 확률 : {round(getPossibility(7, 3), 2)}%')