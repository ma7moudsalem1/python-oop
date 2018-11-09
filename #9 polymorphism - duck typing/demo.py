class Windows:

    def execute(self):
        print("Hello Windows")

class Ubuntu:
    def execute(self):
        print("Hello Ubuntu")

class Computer:

    def __init__(self, software):
        software.execute()

os = Windows()
ub = Ubuntu()
c1 = Computer(ub)