class Compuer:
    plus = 2
    def __init__(self):
        self.ram   = 8


    def clcSpeed(self):
        self.speed = self.ram * self.plus
        print(self.speed)

Compuer.plus = 1
com1 = Compuer()
com1.clcSpeed()
com2 = Compuer()
com2.plus = 3
com2.clcSpeed()