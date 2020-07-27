import pytest
import math
from lesson6.dz.cls import FigureCircles


class TestClassFigureCircles:

    # 1 тест
    @pytest.mark.parametrize("areas", argvalues=[(300, 130)])
    def test_area(self, areas):
        a = areas[0]
        nums_cr = FigureCircles(a, name='Круг')
        area = math.pi * (a**2)
        assert nums_cr.area() == area

    # 2 тест
    @pytest.mark.parametrize("circle_length", argvalues=[(300, 130)])
    def test_circle_length(self, circle_length):
        a = circle_length[0]
        nums_cr = FigureCircles(a, name='Круг')
        circle_length = 2 * math.pi * a
        assert nums_cr.circle_length() == circle_length

    # 3 тест
    @pytest.mark.parametrize("perimeter", argvalues=[(3000, 1300)])
    def test_perimeter(self, perimeter):
        a = perimeter[0]
        nums_cr = FigureCircles(a, name='Круг')
        perimeter = 2 * math.pi * a
        assert nums_cr.perimeter() == perimeter

    # 4 тест
    @pytest.mark.parametrize("fl_a", argvalues=[(3, 100)])
    def test_perimeter(self, fl_a):
        a = fl_a[0]
        nums_cr = FigureCircles(a, name='Круг')
        fl_a = float(a)
        assert nums_cr.fl_a() == fl_a

    # 5 тест
    @pytest.mark.parametrize("add_square", argvalues=[(99, 11)])
    def test_area(self, add_square):
        a = add_square[0]
        nums_cr = FigureCircles(a, name='Круг')
        add_square = math.pi * (a**2)
        assert nums_cr.add_square() == add_square