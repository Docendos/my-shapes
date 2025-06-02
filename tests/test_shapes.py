import math
from app.shapes import Rectangle, Square, Circle, Shape

def test_rectangle():
    r = Rectangle(3, 4)
    assert r.area() == 12
    assert r.perimeter() == 14
    assert isinstance(r, Shape)

def test_square():
    s = Square(5)
    assert s.area() == 25
    assert s.perimeter() == 20
    assert isinstance(s, Rectangle)

def test_circle():
    c = Circle(2)
    assert math.isclose(c.area(), math.pi * 4)
    assert math.isclose(c.perimeter(), 2 * math.pi * 2)
