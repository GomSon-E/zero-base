def getCombination(n, p):
    result = 1

    for i in range(p):
        result *= (n / p)
        n -= 1
        p -= 1

    return result


probability = (getCombination(6, 3) * getCombination(4, 3)) / getCombination(10, 6) * 100
print(f'박스에 \'꽝\'이 적힌 종이가 6장 있고, \'선물\'이 적힌 종이가 4장 있을 때, \'꽝\' 3장과 \'선물\'을 뽑을 확률 : {round(probability, 2)}%')