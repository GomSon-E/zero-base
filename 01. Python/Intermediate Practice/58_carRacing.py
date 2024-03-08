from carRacing import car as c
from carRacing import racing as r

game = r.Racing()

car01 = c.Car('Car01', 'White', 250)
car02 = c.Car('Car02', 'Black', 200)
car03 = c.Car('Car03', 'Yellow', 220)
car04 = c.Car('Car04', 'Red', 280)
car05 = c.Car('Car05', 'Blue', 150)

game.addCar(car01)
game.addCar(car02)
game.addCar(car03)
game.addCar(car04)
game.addCar(car05)

game.startRacing()