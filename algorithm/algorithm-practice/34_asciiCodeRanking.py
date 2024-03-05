data = [32, 'a', 'z', 45, 'G', 39, 50, 'T', 't', 22, 31, 55, 's', 63, 59, 'E']
print(f'data : {data}')

asciiData = []

for d in data:
    if isinstance(d, str):
        asciiData.append(ord(d))
    else:
        asciiData.append(d)

print(f'ascii data : {asciiData}')

rank = [1 for i in range(len(data))]

for i, n1 in enumerate(asciiData):
    for j, n2 in enumerate(asciiData):
        if n1 < n2:
            rank[i] += 1

for i in range(len(rank)):
    if isinstance(data[i], str):
        print(f'data: {data[i]}\t\trank: {rank[i]}')
    else:
        print(f'data: {data[i]}\trank: {rank[i]}')
