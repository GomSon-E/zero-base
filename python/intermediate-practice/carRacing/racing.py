from time import sleep


class Racing:
    def __init__(self):
        self.cars = []
        self.rankings = []

    def startRacing(self):
        for i in range(10):
            print(f'Racing: {i+1}바퀴')

            for c in self.cars:
                c.distance += c.getDistanceForHour()

            sleep(1)
            self.printCurrentCarDistance()

    def printCurrentCarDistance(self):
        for c in self.cars:
            print(f'{c.name}: {c.distance}\t\t', end='')
        print()

    def addCar(self, car):
        self.cars.append(car)