class Computer:

    def __init__(self):
        self.ram = 4

    def update(self):
        self.ram = 8

    def compare(self, other):
        if self.ram == other.ram:
            return True
        return False


com1 = Computer()
com2 = Computer()

if com1.compare(com2):
    print("It's the same")
else:
    print("Not the same")
com1.update()
print("update")
if com1.compare(com2):
    print("It's the same")
else:
    print("Not the same")


