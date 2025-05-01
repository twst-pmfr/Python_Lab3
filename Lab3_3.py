from abc import ABC, abstractmethod
import math

# Абстрактный базовый класс Shape
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


# Конкретная фигура Rectangle (прямоугольник)
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


# Конкретная фигура Circle (круг)
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


# Конкретная фигура Triangle (треугольник)
class Triangle(Shape):
    def __init__(self, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def area(self):
        # Используем формулу Герона для нахождения площади треугольника
        p = (self.side_a + self.side_b + self.side_c) / 2
        return math.sqrt(p * (p - self.side_a) * (p - self.side_b) * (p - self.side_c))

    def perimeter(self):
        return self.side_a + self.side_b + self.side_c


# Полиморфная функция для печати информации о фигуре
def print_shape_info(shape):
    print(f"Тип фигуры: {type(shape).__name__}")
    print(f"Площадь: {shape.area():.2f}")
    print(f"Периметр: {shape.perimeter():.2f}\n")


# Демонстрация полиморфизма
if __name__ == "__main__":
    shapes = [
        Rectangle(4, 5),
        Circle(3),
        Triangle(3, 4, 5)
    ]

    for shape in shapes:
        print_shape_info(shape)