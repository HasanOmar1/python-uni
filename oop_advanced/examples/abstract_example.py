"""
03_abstract_classes_demo.py

This file introduces abstract classes in Python.

Main teaching goals:
1. Explain what abstraction means.
2. Show how to use ABC and abstractmethod.
3. Show that an abstract class cannot be used directly if
   required abstract methods were not implemented.
4. Show how child classes must implement abstract methods.
"""

from abc import ABC, abstractmethod


class Shape(ABC):
    """
    Abstract base class for shapes.
    """

    def __init__(self, name):
        """
        Create a shape.
        in: shape name
        out: Shape object
        """
        self.name = name

    @abstractmethod
    def area(self):
        """
        Return the area of the shape.
        in: none
        out: numeric area
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Return the perimeter of the shape.
        in: none
        out: numeric perimeter
        """
        pass

    def describe(self):
        """
        Print basic shape information.
        in: none
        out: none
        """
        print(f"This is a {self.name}.")


class Rectangle(Shape):
    """
    Rectangle class that must implement all abstract methods.
    """

    def __init__(self, width, height):
        """
        Create a rectangle.
        in: width and height
        out: Rectangle object
        """
        super().__init__("Rectangle")
        self.width = width
        self.height = height

    def area(self):
        """
        Calculate rectangle area.
        in: none
        out: area
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculate rectangle perimeter.
        in: none
        out: perimeter
        """
        return 2 * (self.width + self.height)


class Circle(Shape):
    """
    Circle class that must implement all abstract methods.
    """

    def __init__(self, radius):
        """
        Create a circle.
        in: radius
        out: Circle object
        """
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        """
        Calculate circle area.
        in: none
        out: area
        """
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        """
        Calculate circle perimeter.
        in: none
        out: perimeter
        """
        return 2 * 3.14 * self.radius


def main():
    """
    Run examples for abstract classes.
    in: none
    out: none
    """
    rectangle = Rectangle(5, 3)
    circle = Circle(4)

    print("=== RECTANGLE ===")
    rectangle.describe()
    print("Area:", rectangle.area())
    print("Perimeter:", rectangle.perimeter())

    print("\n=== CIRCLE ===")
    circle.describe()
    print("Area:", circle.area())
    print("Perimeter:", circle.perimeter())

    print("\n=== IMPORTANT NOTE ===")
    print("You cannot create Shape() directly because it is abstract.")
    print("Shape is used as a blueprint for other classes.")


if __name__ == "__main__":
    main()