import pytest
from lesson6.dz.cls import FigureRectangle


class TestClassFigureRectangle:

    # 1 тест
    @pytest.mark.parametrize("areas", argvalues=[(5, 23), (45, 117)])
    def test_area(self, areas):
        a = areas[0]
        b = areas[1]
        nums_pr = FigureRectangle(a, b, c=99, d=44, name='Прямоугольник')
        area = a * b
        assert nums_pr.area() == area

    # 2 тест
    @pytest.mark.parametrize("angles", argvalues=[(890, 234, 5678, 88), (100, 1100, 5600, 77)])
    def test_angles(self, angles):
        a = angles[0]
        b = angles[1]
        c = angles[2]
        d = angles[3]
        nums_pr = FigureRectangle(a, b, c, d, name='Прямоугольник')
        angless = a, b, c, d
        assert nums_pr.angles() == angless

    # 3 тест
    @pytest.mark.parametrize("perimeter", argvalues=[(100, 200), (41, 11)])
    def test_perimeter(self, perimeter):
        a = perimeter[0]
        b = perimeter[1]
        nums_pr = FigureRectangle(a, b, c=5, d=8, name='Прямоугольник')
        perimeters = (a + b) * 2
        assert nums_pr.perimeter() == perimeters

    # 4 тест
    @pytest.mark.parametrize("sum", argvalues=[(890, 234, 5678, 88), (100, 1100, 5600, 77)])
    def test_sum(self, sum):
        a = sum[0]
        b = sum[1]
        c = sum[2]
        d = sum[3]
        nums_pr = FigureRectangle(a, b, c, d, name='Прямоугольник')
        sum = a + b + c + d
        assert nums_pr.sum() == sum

    # 5 тест
    @pytest.mark.parametrize("add_square", argvalues=[(99, 33), (9, 2)])
    def test_add_square(self, add_square):
        a = add_square[0]
        b = add_square[1]
        nums_pr = FigureRectangle(a, b, c=50, d=7, name='Прямоугольник')
        add_square = a * b
        assert nums_pr.add_square == add_square