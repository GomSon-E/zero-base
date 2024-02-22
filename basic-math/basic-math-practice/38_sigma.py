an = 1
sn = 0
for i in range(30):
    an *= 2
    sn += an

    print(f'{i + 1}번째의 항: {an}')
    print(f'{i + 1}번째까지의 합: {sn}')
