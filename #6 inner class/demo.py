class Compuer:

    def __init__(self, ram, cpu):
        self.ram = ram
        self.cpu = cpu
        self.lap = self.Laptop("Dell")

    def info(self):
        print(self.ram, self.cpu)
        self.lap.info()

    class Laptop:
        def __init__(self, brand):
            self.brand = brand

        def info(self):
            print(self.brand)

c1 = Compuer(4, "core 5")

c1.info()
c1.lap.info()

lap1 = Compuer.Laptop("HP")
lap1.info()
