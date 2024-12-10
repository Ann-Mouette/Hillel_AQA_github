"""
1. Генератори.

Напишіть генератор, який повертає послідовність парних
чисел від 0 до N.
Створіть генератор, який генерує послідовність Фібоначчі
до певного числа N.

2. Ітератори.

Реалізуйте ітератор для зворотного виведення елементів списку.
Напишіть ітератор, який повертає всі парні числа в діапазоні
від 0 до N.

3. Декоратори.

Напишіть декоратор, який логує аргументи та результати
викликаної функції.
Створіть декоратор, який перехоплює та обробляє винятки,
які виникають в ході виконання функції.
"""


# Task 1
def even_numbers(n):
    """Generate even numbers from 0 to N."""
    for num in range(0, n + 1, 2):
        yield num


# Example
for number in even_numbers(50):
    print(number)


def fibonacci(n):
    """Generate Fibonacci numbers up to N."""
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b


# Example
for number in fibonacci(45):
    print(number)


# Task 2
class ReverseIterator:
    """Iterator for reversing the list elements."""

    def __init__(self, data):
        """Initialize the iterator with the list to reverse."""
        self.data = data
        self.index = len(data) - 1

    def __iter__(self):
        """Return the iterator object."""
        return self

    def __next__(self):
        """Return the next element in reverse order."""
        if self.index < 0:
            raise StopIteration
        value = self.data[self.index]
        self.index -= 1
        return value


# Example
for item in ReverseIterator([1, 2, 'book', 'dog', 0.7]):
    print(item)


class EvenIterator:
    """Iterator for even numbers from 0 to N."""

    def __init__(self, n):
        """Initialize the iterator."""
        self.n = n
        self.current = 0

    def __iter__(self):
        """Return the iterator object."""
        return self

    def __next__(self):
        """Return the next even number in the range."""
        if self.current > self.n:
            raise StopIteration
        value = self.current
        self.current += 2
        return value


# Example
for number in EvenIterator(67):
    print(number)


def logger(func):
    """Create decorator for logging function arguments and results."""
    def wrapper(*args, **kwargs):
        """Wrap the function and log its arguments and result."""
        print(f'{func.__name__} called with arguments: {args}, {kwargs}')
        result = func(*args, **kwargs)
        print(f'Result: {result}')
        return result
    return wrapper


# Example
@logger
def add(a, b):
    """Multiply two numbers."""
    return a * b


add(7, 8)


def exception_handler(func):
    """Create decorator for exception handling."""
    def wrapper(*args, **kwargs):
        """Wrap the function and handle exceptions."""
        try:
            return func(*args, **kwargs)
        except Exception as error:
            print('Exception in function:', func.__name__)
            print('Error:', error)
    return wrapper


# Example
@exception_handler
def divide(a, b):
    """Divide two numbers."""
    return a / b


divide(31, 0)
