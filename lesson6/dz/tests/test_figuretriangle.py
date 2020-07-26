import pytest
from lesson6.dz.cls import FigureTriangle


class TestClassFigureTriangle:

    # 1 тест
    @pytest.mark.parametrize("areas", argvalues=[(5, 23), (45, 117)])
    def test_area(self, areas):
        a = areas[0]
        b = areas[1]
        nums_tr = FigureTriangle(a, b, c=56, name='Треугольник')
        area = (a * b) / 2
        assert nums_tr.area() == area

    # 2 тест
    @pytest.mark.parametrize("angles", argvalues=[(5, 23, 6), (45, 117, 56)])
    def test_angles(self, angles):
        a = angles[0]
        b = angles[1]
        c = angles[2]
        nums_tr = FigureTriangle(a, b, c, name='Треугольник')
        angless = a, b, c
        assert nums_tr.angles() == angless

    # 3 тест
    @pytest.mark.parametrize("perimeter", argvalues=[(100, 200, 700), (41, 11, 23)])
    def test_perimeter(self, perimeter):
        a = perimeter[0]
        b = perimeter[1]
        c = perimeter[2]
        nums_tr = FigureTriangle(a, b, c, name='Треугольник')
        perimeters = a + b + c
        assert nums_tr.perimeter() == perimeters

    # 4 тест
    @pytest.mark.parametrize("half_perimeter", argvalues=[(10, 20, 70), (4, 1, 2)])
    def test_half_perimeter(self, half_perimeter):
        a = half_perimeter[0]
        b = half_perimeter[1]
        c = half_perimeter[2]
        nums_tr = FigureTriangle(a, b, c, name='Треугольник')
        half_perimeters = (a + b + c) / 2.0
        assert nums_tr.half_perimeter() == half_perimeters

    # 5 тест
    @pytest.mark.parametrize("add_square", argvalues=[(99, 33), (9, 2)])
    def test_add_square(self, add_square):
        a = add_square[0]
        b = add_square[1]
        nums_tr = FigureTriangle(a, b, c=50, name='Треугольник')
        add_square = (a * b) / 2
        assert nums_tr.add_square == add_square