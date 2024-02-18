class Member:
    def __init__(self, nickname, password):
        self.nickname = nickname
        self.password = password

class MemberRepository:
    def __init__(self):
        self.members = {}

    def addMember(self, member):
        self.members[member.nickname] = member.password

    def loginMember(self, nickname, password):
        if (nickname in self.members
                and self.members[nickname] == password):
            print(f'{nickname}: login success!!')
        else:
            print(f'{nickname}: login fail!!')

    def removeMember(self, nickname):
        del self.members[nickname]

    def printMembers(self):
        for k in self.members.keys():
            print(f'ID : {k}')
            print(f'PW : {self.members[k]}')