dic = {}

def addMember():
    for i in range(5):
        email = input('메일 입력: ')
        password = input('비밀번호 입력: ')
        dic[email] = password

    for key in dic.keys():
        print(f'{key} : {dic[key]}')

def deleteMember():
    for i in range(3):
        email = input('메일 입력: ')

        if email in dic:
            password = input('비밀번호 입력: ')

            if dic[email] == password:
                del dic[email]
                print(f'{email}님 삭제 완료!!')
            else:
                print('비밀번호 확인 요망!!')

        else:
            print('계정 확인 요망!')


addMember()
deleteMember()
