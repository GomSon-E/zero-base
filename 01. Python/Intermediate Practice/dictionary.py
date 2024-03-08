from abc import *

class AbsDictionary(metaclass=ABCMeta):
    def __init__(self):
        self.wordDic = {}

    @abstractmethod
    def registerWord(self, korean, other):
        pass

    @abstractmethod
    def removeWord(self, korean):
        pass

    @abstractmethod
    def updateWord(self, korean, other):
        pass

    @abstractmethod
    def searchWord(self, korean):
        pass

class KorToEngDictionary(AbsDictionary):
    def __init__(self):
        super().__init__()

    def registerWord(self, korean, english):
        self.wordDic[korean] = english

    def removeWord(self, korean):
        del self.wordDic[korean]

    def updateWord(self, korean, english):
        if korean in self.wordDic:
            self.wordDic[korean] = english
        else:
            print('Not Found!!')

    def searchWord(self, korean):
        if korean in self.wordDic:
            return self.wordDic[korean]
        else:
            print('Not Found!!')

    def printWords(self):
        for word in self.wordDic:
            print(f'({word}, {self.wordDic[word]})')