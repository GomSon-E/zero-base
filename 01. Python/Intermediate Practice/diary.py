import time

uri = 'files/'

class LoginFailException(Exception):
    def __init__(self):
        super().__init__('Login Fail!!')


class Member:
    def __init__(self, nickname, password):
        self.nickname = nickname
        self.password = password


class MemberRepository:
    def __init__(self):
        self.memberDic = {}

    def addMember(self, member):
        self.memberDic[member.nickname] = member.password

    def loginMember(self, nickname, password):
        if nickname in self.memberDic \
                and self.memberDic[nickname] == password:
            print('Login Success!!')
        else:
            raise LoginFailException


def addDiary(nickname):
    content = input('오늘 하루 인상 깊은 일을 기록하세요.\t')

    with open(uri + nickname + '.txt', 'a', encoding='utf-8') as f:
        f.write(f'[{time.strftime("%Y-%m-%d %I:%M:%S %p", time.localtime())}] {content}\n')

def readDiary(nickname):
    with open(uri + nickname + '.txt', 'r', encoding='utf-8') as f:
        content = f.readline()

        while content != '':
            print(content, end='')
            content = f.readline()
