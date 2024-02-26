numbers = [4, 6, 7, 9]
result = []

for i in numbers:
    for j in numbers:
        for k in numbers:
            if i != j and i != k and j != k:
                result.append([i, j, k])

print(f'result: {result}')
print(f'result length: {len(result)}')