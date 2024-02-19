num = int(input('0보다 큰 정수 입력: '))

divisorList = []

for i in range(1, num + 1):
    if num % i == 0:
        divisorList.append(i)

with open('files/divisorRecord.txt', 'a', encoding='utf-8') as f:
    f.write(f'{num}의 약수: {divisorList}\n')

print('divisor write complete!')