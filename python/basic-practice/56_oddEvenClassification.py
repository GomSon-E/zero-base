for i in range(1, 101) :
    if i < 10:
        if i % 2 == 0:
            print('[{}]: 짝수!'.format(i))
        else :
            print('[{}]: 홀수!'.format(i))
    else:
        print('[{}]'.format(i), end=' ')
        print('십의 자리:', end=' ')
        if i // 10 % 2 == 0 :
            print('짝수!!', end=' ')
        else :
            print('홀수!!', end=' ')
        print('일의 자리:', end=' ')
        if i % 10 == 0 :
            print('0', end=' ')
        elif i % 10 % 2 == 0 :
            print('짝수!!', end=' ')
        else :
            print('홀수!!', end=' ')

        print()