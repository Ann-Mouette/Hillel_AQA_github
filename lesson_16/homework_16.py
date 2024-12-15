"""
Виконання домашнього завдання 16.

Завдання 1, 2.
"""

import math
from abc import ABC, abstractmethod

"""
Task 1.

Створіть клас Employee, який має атрибути name та salary.
Далі створіть два класи, Manager та Developer, які успадковуються
від Employee. Клас Manager повинен мати додатковий атрибут
department, а клас Developer - атрибут programming_language.
Тепер створіть клас TeamLead, який успадковується як від Manager,
так і від Developer. Цей клас представляє керівника з команди
розробників. Клас TeamLead повинен мати всі атрибути як Manager
(ім'я, зарплата, відділ), а також атрибут team_size, який вказує
на кількість розробників у команді, якою керує керівник.
Напишіть тест, який перевіряє наявність атрибутів з Manager
та Developer у класі TeamLead.

Task 2.

Створіть абстрактний клас "Фігура" з абстрактними методами
для отримання площі та периметру. Наслідуйте від нього декілька
(> 2) інших фігур, та реалізуйте математично вірні для них методи
для площі та периметру. Властивості по типу “довжина сторони” й т.д.
повинні бути приватними, та ініціалізуватись через конструктор.
Створіть Декілька різних об’єктів фігур, та у циклі порахуйте
та виведіть в консоль площу та периметр кожної.
"""


# Task 1
class Employee:
    """Represents Employee with name and salary."""

    def __init__(self, name, salary, **kwargs):
        """Initialize Employee."""
        self.name = name
        self.salary = salary
        super().__init__(**kwargs)


class Manager(Employee):
    """Represents Manager who has a department."""

    def __init__(self, department, **kwargs):
        """Initialize Manager."""
        self.department = department
        super().__init__(**kwargs)


class Developer(Employee):
    """Represents Developer with programming language."""

    def __init__(self, programming_language: str, **kwargs):
        """Initialize Developer."""
        self.programming_language = programming_language
        super().__init__(**kwargs)


class TeamLead(Manager, Developer):
    """Represents TeamLead who manages a development team."""

    def __init__(self, team_size: int, **kwargs):
        """Initialize TeamLead."""
        self.team_size = team_size
        super().__init__(**kwargs)


def test_team_lead_attributes():
    """Test TeamLead class correctly initializes and retains attributes."""
    lead = TeamLead(
        name='Smith',
        salary=7000,
        department='Development',
        programming_language='Python',
        team_size=6,
    )
    assert lead.name == 'Smith', 'Incorrect name attribute'
    assert lead.salary == 7000, 'Incorrect salary attribute'
    assert lead.department == 'Development', 'Incorrect department attribute'
    assert lead.programming_language == 'Python', 'Incorrect language'
    assert lead.team_size == 6, 'Incorrect team_size attribute'


# Task 2


class Shape(ABC):
    """Represents class Shape."""

    @abstractmethod
    def area(self):
        """Calculate the area of the Shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate the perimeter of the Shape."""
        pass


class Circle(Shape):
    """Represents a Circle."""

    def __init__(self, radius):
        """Initialize a Circle with a radius."""
        self.__radius = radius  # Private attribute for the radius

    def area(self):
        """Calculate the area of the Circle."""
        return math.pi * self.__radius**2

    def perimeter(self):
        """Calculate the perimeter of the Circle."""
        return 2 * math.pi * self.__radius


class Rectangle(Shape):
    """Represents a Rectangle."""

    def __init__(self, length, width):
        """Initialize a Rectangle with length and width."""
        self.__length = length
        self.__width = width

    def area(self):
        """Calculate the area of the Rectangle."""
        return self.__length * self.__width

    def perimeter(self):
        """Calculate the perimeter of the Rectangle."""
        return 2 * (self.__length + self.__width)


class Square(Shape):
    """Represents a Square."""

    def __init__(self, side):
        """Initialize a Square with a side length."""
        self.__side = side

    def area(self):
        """Calculate the area of the Square."""
        return self.__side**2

    def perimeter(self):
        """Calculate the perimeter of the Square."""
        return 4 * self.__side


if __name__ == '__main__':
    shapes = [
        Circle(5),
        Rectangle(4, 7),
        Square(3),
    ]

    for shape in shapes:
        print(f'{shape.__class__.__name__}:')
        print(f'  Area: {shape.area():.2f}')
        print(f'  Perimeter: {shape.perimeter():.2f}')
