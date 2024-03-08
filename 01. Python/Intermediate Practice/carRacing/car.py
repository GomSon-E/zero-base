import random

class Car:
    def __init__(self, name, color, speed):
        self.name = name
        self.color = color
        self.max_speed = speed
        self.distance = 0

    def printCarInfo(self):
        print(f'name: {self.name}, color: {self.color}, max_speed: {self.max_speed}')

    def controlSpeed(self):
        return random.randint(0, self.max_speed)

    def getDistanceForHour(self):
        return self.controlSpeed() * 1