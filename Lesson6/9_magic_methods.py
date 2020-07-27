class Beauty:

    def __init__(self, amount):
        self.amount = amount

    def __repr__(self):
        return "={ Beauty }="

    def __str__(self):
        return "{B*E*A*U*T*Y}"

    def __add__(self, other):
        return str(self) + " and " + str(other)

    def __eq__(self, other):
        return self.amount == other.amount

    def __call__(self, *args):
        return str(self) + " got args " + str(args)


b1 = Beauty(100)
b2 = Beauty(100)

print(b1 + b2)
print(b1 == b2)

print(b1("BOOOOO"))
print(repr(b1))