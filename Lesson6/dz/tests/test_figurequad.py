import pytest
from lesson6.dz.cls import FigureQuad


class TestClassFigureQuad:

    # 1 тест
    @pytest.mark.parametrize("areas", argvalues=[(30, 133)])
    def test_area(self, areas):
        a = areas[0]
        nums_qd = FigureQuad(a, b=6, c=99, d=44, name='Квадрат')
        area = a * a
        assert nums_qd.area() == area

    # 2 тест
    @pytest.mark.parametrize("angles", argvalues=[(890, 234, 5678, 88), (100, 1100, 5600, 77)])
    def test_angles(self, angles):
        a = angles[0]
        b = angles[1]
        c = angles[2]
        d = angles[3]
        nums_qd = FigureQuad(a, b, c, d, name='Квадрат')
        angless = a, b, c, d
        assert nums_qd.angles() == angless

    # 3 тест
    @pytest.mark.parametrize("perimeter", argvalues=[(100, 11)])
    def test_perimeter(self, perimeter):
        a = perimeter[0]
        nums_qd = FigureQuad(a, b=5, c=5, d=8, name='Квадрат')
        perimeters = a * 4
        assert nums_qd.perimeter() == perimeters

    # 4 тест
    @pytest.mark.parametrize("sum", argvalues=[(890, 234, 5678, 88), (100, 1100, 5600, 77)])
    def test_sum(self, sum):
        a = sum[0]
        b = sum[1]
        c = sum[2]
        d = sum[3]
        nums_qd = FigureQuad(a, b, c, d, name='Квадрат')
        sum = a + b + c + d
        assert nums_qd.sum() == sum

    # 5 тест
    @pytest.mark.parametrize("add_square", argvalues=[(99, 2)])
    def test_add_square(self, add_square):
        a = add_square[0]
        nums_qd = FigureQuad(a, b=8, c=50, d=7, name='Квадрат')
        add_square = a * a
        assert nums_qd.add_square == add_square