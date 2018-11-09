class Adding:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def __add__(self, other):
        r1 = self.n1 + other.n1
        r2 = self.n2 + other.n2
        r  = Adding(r1, r2)
        return r

    def __gt__(self, other):
        r1 = self.n1 + self.n2
        r2 = other.n2 + other.n2
        if r1 > r2:
            return True
        else:
            return False

    def __str__(self):
        return "{} , {}".format(self.n1, self.n2)

s1 = Adding(22, 18)
s2 = Adding(19, 16)
s3 = s1 + s2
print(s3.n2)

if s1 > s2:
    print("S1 greater that S2")
else:
    print("S2 greater than S1")

print(s1)
