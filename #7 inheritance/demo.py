class Machine:
    def machineType(self):
        print("Dos")


class Computer(Machine):
    def cpu(self):
        print("computer cpu")

    def ram(self):
        print("computer ram")

class OS:
    def osName(self):
        print("Windows")

class Laptop(Computer, OS):
    def brand(self):
        print("Dell")

c1 = Laptop()
c1.cpu()
c1.machineType()
c1.osName()