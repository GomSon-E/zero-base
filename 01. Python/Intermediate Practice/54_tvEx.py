import tv

my4kTv = tv.Tv4k(65, 'silver')
my4kTv.setSmartTv('on')
my4kTv.turnOn()
my4kTv.printTvInfo()
my4kTv.turnOff()

print()

your4kTv = tv.Tv4k(55, 'white')
your4kTv.setSmartTv('off')
your4kTv.turnOn()
your4kTv.printTvInfo()
your4kTv.turnOff()

print()

my8kTv = tv.Tv8k(75, 'black')
my8kTv.setSmartTv('on')
my8kTv.setAiTv('on')
my8kTv.turnOn()
my8kTv.printTvInfo()
my8kTv.turnOff()

print()

your8kTv = tv.Tv8k(85, 'red')
your8kTv.setSmartTv('on')
your8kTv.setAiTv('off')
your8kTv.turnOn()
your8kTv.printTvInfo()
your8kTv.turnOff()