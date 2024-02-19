import random
from time import sleep

class Music:
    def __init__(self, title, singer, play_time):
        self.title = title
        self.singer = singer
        self.play_time = play_time

    def printSongInfo(self):
        print(f'Title: {self.title}\tSinger: {self.singer}\t[{self.play_time}sec]')

class Player:
    def __init__(self):
        self.playList = []
        self.isLoop = False

    def addSong(self, song):
        self.playList.append(song)

    def play(self):
        while True:
            for song in self.playList:
                song.printSongInfo()
                sleep(song.play_time)
            if not self.isLoop:
                break

    def shuffle(self):
        random.shuffle(self.playList)

    def setIsLoop(self, flag):
        self.isLoop = flag