class EmptyException(Exception):
    def __init__(self, info):
        super().__init__(f'{info} is empty!')

def signIn(info):
    for k in info.keys():
        if info[k] == '':
            raise EmptyException(k)

    print('Membership Completed!')
    for k in info.keys():
        print(f'{k}: {info[k]}')


memberInfo = {}

memberInfo['name'] = input('이름 입력: ')
memberInfo['email'] = input('이메일 입력: ')
memberInfo['password'] = input('비밀번호 입력: ')
memberInfo['address'] = input('주소 입력: ')
memberInfo['phoneNum'] = input('연락처 입력: ')

try:
    signIn(memberInfo)
except EmptyException as e:
    print(e)



