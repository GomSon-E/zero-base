num = int(input('0보다 큰 정수 입력: '))

primeList = []

for i in range(2, num + 1):
    flag = True

    for j in range(2, i):
        if i % j == 0:
            flag = False
            break

    if flag:
        primeList.append(i)

with open('files/primeRecord.txt', 'a', encoding='utf-8') as f:
    f.write(f'{num}까지의 소수: {primeList}\n')

print('prime write complete!')