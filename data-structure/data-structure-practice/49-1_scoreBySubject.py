subject = ['국어', '영어', '수학', '과학', '국사']
scores = {}

for s in subject:
    scores[s] = int(input(f'{s} 점수 입력: '))

print(f'과목별 점수: {scores}')