class Computer:
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def info(self):
        print("Cpu:", self.cpu, "Ram:", self.ram)

com1 = Computer("Core 5", 4)
com2 = Computer("Core 7", 8)
com1.info()
com2.info()
