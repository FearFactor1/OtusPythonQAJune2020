import math


class FigureTriangle:

    def __init__(self, a, b, c, name):
        self.a = a
        self.b = b
        self.c = c
        self.name = name

    name = "Треугольник"

    def area(self):
        return (self.a * self.b) / 2

    def angles(self):
        return self.a, self.b, self.c

    def perimeter(self):
        return self.a + self.b + self.c

    def half_perimeter(self):
        return (self.a + self.b + self.c) / 2.0

    @property
    def add_square(self):
        if self.name == 'Треугольник':
            return self.area()
        else:
            raise AssertionError('wrong class')


class FigureRectangle:

    def __init__(self, a, b, c, d, name):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.name = name

    name = "Прямоугольник"

    def area(self):
        return self.a * self.b

    def angles(self):
        return self.a, self.b, self.c, self.d

    def perimeter(self):
        return (self.a + self.b) * 2

    def sum(self):
        return self.a + self.b + self.c + self.d

    @property
    def add_square(self):
        if self.name == 'Прямоугольник':
            return self.area()
        else:
            raise AssertionError('wrong class')


class FigureQuad(FigureRectangle):

    def __init__(self, a, b, c, d, name):
        super().__init__(a, b, c, d, name)

    name = "Квадрат"

    def area(self):
        return self.a * self.a

    def angles(self):
        return self.a, self.b, self.c, self.d

    def perimeter(self):
        return self.a * 4

    def sum(self):
        return self.a + self.b + self.c + self.d

    @property
    def add_square(self):
        if self.name == 'Квадрат':
            return self.area()
        else:
            raise AssertionError('wrong class')


class FigureCircles:

    def __init__(self, a, name):
        self.a = a
        self.name = name

    name = "Круг"

    def area(self):
        return math.pi * (self.a**2)

    def circle_length(self):
        return 2 * math.pi * self.a

    def perimeter(self):
        return 2 * math.pi * self.a

    def fl_a(self):
        return float(self.a)

    @property
    def add_square(self):
        if self.name == 'Круг':
            return self.area()
        else:
            raise AssertionError('wrong class')


treugolnik = FigureTriangle(a=4, b=4, c=4, name='Треугольник')
print(treugolnik.add_square)

prymougolnik = FigureRectangle(a=2, b=2, c=2, d=2, name='Прямоугольник')
print(prymougolnik.add_square)

kvadrat = FigureQuad(a=10, b=10, c=2, d=2, name='Квадрат')
print(kvadrat.add_square)

krug = FigureCircles(a=50, name='Круг')
print(krug.add_square)