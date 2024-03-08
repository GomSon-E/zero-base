def template(p, t, r, total):
    print('=' * 45)
    print(f'예치금\t: {format(p, ',')}원')
    print(f'예치기간\t: {t}년')
    print(f'연 이율\t: {r}%')
    print('-' * 45)
    print(f'{t}년 후 총 수령액: {format(total, ',')}원')
    print('=' * 45)

def simpleInterest(p, t, r):
    print('\n[단리 계산기]')
    total = int(p + (p * t * (r / 100)))
    template(p, t, r, total)

def monthlyCompoundInterest(p, t, r):
    print('\n[월복리 계산기]')
    total = int(p * (1 + (r / 100 / 12)) ** (t * 12))
    template(p, t, r, total)


principal = int(input('예치금(원): '))
time = int(input('기간(년): '))
interest = int(input('연 이율(%): '))

simpleInterest(principal, time, interest)
monthlyCompoundInterest(principal, time, interest)