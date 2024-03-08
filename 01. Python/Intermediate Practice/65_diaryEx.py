import diary

mr = diary.MemberRepository()

while True:
    choice = int(input('1. 회원가입\t\t2. 한줄일기쓰기\t\t3. 한줄일기보기\t\t4. 종료\t\t'))

    if choice == 1:
        nickname = input('ID 입력: ')
        password = input('비밀번호 입력: ')
        newMember = diary.Member(nickname, password)
        mr.addMember(newMember)

    elif choice == 2:
        nickname = input('ID 입력: ')
        password = input('비밀번호 입력: ')
        try:
            mr.loginMember(nickname, password)
        except Exception as e:
            print(e)
        diary.addDiary(nickname)

    elif choice == 3:
        nickname = input('ID 입력: ')
        password = input('비밀번호 입력: ')
        try:
            mr.loginMember(nickname, password)
        except Exception as e:
            print(e)
        diary.readDiary(nickname)

    elif choice == 4:
        print('Bye!!')
        break

    else:
        print('잘못된 입력값 입니다.')