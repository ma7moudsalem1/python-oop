class Computer:
    def __init__(self):
        self.ram = 4

    def info(self):
        print("this is method belongs to computer class")

class OS:
    def __init__(self):
        print("OS Begin")

    def info(self):
        print("this is method belongs to OS class")

class Laptop(Computer, OS):

    def __init__(self):
        super().__init__()
        self.ram = self.ram + 4

    def info(self):
        print(self.ram)
        super().info()
        print("this is method belongs to Laptop class")

lap = Laptop()
lap.info()