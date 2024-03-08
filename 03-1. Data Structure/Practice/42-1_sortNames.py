nameList = []

for i in range(5):
    nameList.append(input('친구 이름 입력: '))

print(f'친구들: {nameList}')
nameList.sort()
print(f'오름차순: {nameList}')
nameList.sort(reverse=True)
print(f'내림차순: {nameList}')