class NormalTv:
    def __init__(self, inch=32, color='black', resolution='FHD'):
        self.inch = inch
        self.color = color
        self.resolution = resolution
        self.smartTv = 'off'
        self.aiTv = 'off'

    def turnOn(self):
        print("TV Power On!!")

    def turnOff(self):
        print("TV Power Off!!")

    def printTvInfo(self):
        print(f'inch: {self.inch}')
        print(f'color: {self.color}')
        print(f'resolution: {self.resolution}')
        print(f'smartTv: {self.smartTv}')
        print(f'aiTv: {self.aiTv}')

class Tv4k(NormalTv):
    def __init__(self, inch, color, resolution='4K'):
        super().__init__(inch, color, resolution)

    def setSmartTv(self, smart):
        self.smartTv = smart


class Tv8k(NormalTv):
    def __init__(self, inch, color, resolution='8K'):
        super().__init__(inch, color, resolution)

    def setSmartTv(self, smart):
        self.smartTv = smart

    def setAiTv(self, ai):
        self.aiTv = ai