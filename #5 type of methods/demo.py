class Computer:
    company = "Dell"

    def __init__(self):
        print("Init")

    def getCpu(self):
        return self.cpu

    def setCpu(self, cpu):
        self.cpu = cpu

    @classmethod
    def getCompanyName(cls):
        return cls.company

    @staticmethod
    def info():
        print("this is computer class")

c1 = Computer()
c1.setCpu("core 7")
print(c1.getCpu())
print(Computer.getCompanyName())
Computer.info()