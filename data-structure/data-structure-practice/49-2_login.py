members = {'urkpo': '0928^7$',
           'xxayv': '%2*9$1',
           'lsqvx': '!0%)&&4',
           'heums': '%@3^0%3',
           'uwcmx': '85236(&'}

nickname = input('ID 입력: ')
password = input('비밀번호 입력: ')

if nickname in members.keys():
    if members[nickname] == password:
        print('로그인 성공!!')
    else:
        print('비밀번호 확인!!')
else:
    print('아이디 확인!!')