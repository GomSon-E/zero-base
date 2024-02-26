numbers = [4, 6, 7, 9]
result = []

for i in numbers:
    for j in numbers:
        if i != j:
            result.append([i, j])

print(f'result: {result}')
print(f'result length: {len(result)}')