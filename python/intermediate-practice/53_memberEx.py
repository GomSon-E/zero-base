import member as mb

mr = mb.MemberRepository()

for i in range(3):
    nickname = input('아이디 입력 : ')
    password = input('비밀번호 입력 : ')
    member = mb.Member(nickname, password)
    mr.addMember(member)

mr.printMembers()

mr.loginMember('abc@gmail.com', '1234')
mr.loginMember('def@gmail.com', '5678')
mr.loginMember('ghi@gmail.com', '9012')

mr.removeMember('abc@gmail.com')

mr.printMembers()