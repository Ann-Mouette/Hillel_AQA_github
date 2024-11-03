"""
Homework №07_01.

Tasks 1-10
"""

# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити  або доповнити.
"""


def multiplication_table(number):
    """
    Print the multiplication table for a given number.

    Parameters:
    number (int): The number for which the multiplication
    table is generated.

    Returns:
    None: This function does not return a value;
    it only prints each line of the multiplication table
    until the product exceeds 25.
    """
    # Initialize the appropriate variable
    multiplier = 1
    while True:
        result = number * multiplier
        if result > 25:
            break
        print(str(number) + 'x' + str(multiplier) + '=' + str(result))
        multiplier += 1


multiplication_table(3)


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""


def count_sum(a, b):
    """
    Calculate the sum of two numbers and prints the result.

    Parameters:
    a (float or int): The first number.
    b (float or int): The second number.

    Returns:
    None: This function does not return a value; it only prints the result.
    """
    res = a + b
    print('Result:', res)


count_sum(3, 2)

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""


def count_average(numbers):
    """
    Calculate the arithmetic mean (average) of a list of numbers.

    Parameters:
    numbers (list of float or int): A list of numerical values.

    Returns:
    float: The arithmetic mean of the list. Returns 0 if the list is empty.
    """
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


# Example:
numbers = [1, 2, 3, 4, 5]
print(count_average(numbers))

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""


def reverse_string(text):
    """
    Reverse the given string.

    Parameters:
    text (str): The string to be reversed.

    Returns:
    str: The input string in reverse order.
    """
    return text[::-1]


# Example:
text = 'Hello'
print(reverse_string(text))

# task 5
"""Написати функцію, яка приймає список слів та
повертає найдовше слово у списку.
"""


def find_longest_words(words):
    """
    Find the longest word(s) in a list of words.

    Parameters:
    words (list of str): A list of words to search for
    the longest word.

    Returns:
    list of str: A list containing the longest word(s).
    If multiple words have the same maximum length,
    all such words are included in the returned list.
    """
    longest_words = []
    max_length = 0

    for word in words:
        if len(word) > max_length:
            max_length = len(word)
            longest_words = [word]
        elif len(word) == max_length:
            longest_words.append(word)

    return longest_words


# Example:
words = ['apple', 'acer', 'htc', 'nokia']
print(find_longest_words(words))

# task 6
"""Написати функцію, яка приймає два рядки та повертає
індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого
рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""


def find_substring(string_main, substring):
    """
    Return the index of the 1st occurrence of a substring within a string.

    This function searches for the specified substring within the main string.
    If the substring is found, the function returns the index of
    its first occurrence.
    If the substring is not found, the function returns -1.

    Parameters:
    string_main (str): The main string in which to search for the substring.
    substring (str): The substring to find within the main string.

    Returns:
    int: The index of the first occurrence of the substring if found,
    otherwise -1.
    """
    return string_main.find(substring)


string_main = 'I like broccoli and cilantro!'
substring = 'broccoli'
print(find_substring(string_main, substring))

str1 = 'Lorem ipsum dolor sit amet, consectetur adipiscing'
str2 = 'Fusce quis'
print(find_substring(str1, str2))

# task 7
# task 8
# task 9
# task 10
"""Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення
та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""

# task 7
"""Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""


def calculate_goods_per_stock(all_stock, stock_1_2, stock_2_3):
    """
    Calculate the number of goods in each of the warehouses.

    Parameters:
    all_stock (int): The total number of goods in three warehouses.
    stock_1_2 (int): The number of goods in the first
    and second warehouses together.
    stock_2_3 (int): The number of goods in the second
    and third warehouses together.

    Returns:
    dict: dictionary with the number of goods in
    each warehouse (keys: 'stock one', 'stock two', 'stock three').
    """
    # Number of goods in the third warehouse:
    stock_3 = all_stock - stock_1_2

    # Number of goods in the second warehouse:
    stock_2 = stock_2_3 - stock_3

    # Number of goods in the first warehouse:
    stock_1 = stock_1_2 - stock_2

    # Return the results in the form of a dictionary
    return {
        'stock one': stock_1,
        'stock two': stock_2,
        'stock three': stock_3,
    }


# Example
all_stock = 375291
stock_1_2 = 250449
stock_2_3 = 222950

result = calculate_goods_per_stock(all_stock, stock_1_2, stock_2_3)
print(result)


# task 8
"""Exists some car data with color, year, engine_volume, car type , price
We have search_criteria as tuple of ( year>= , engine_volume >= , price<=)
write code that will help us to get cars that satisfy search_criteria.
Cars should be sorted by price ascending.
We should print up to five (5) first found elements
car_data = {
    'Mercedes': ('silver', 2019, 1.8, 'sedan', 50000),
    'Audi': ('black', 2020, 2.0, 'sedan', 55000),
    'BMW': ('white', 2018, 3.0, 'suv', 70000),
    'Lexus': ('gray', 2016, 2.5, 'coupe', 45000),
    'Toyota': ('blue', 2021, 1.6, 'hatchback', 25000),
    'Honda': ('red', 2017, 1.5, 'sedan', 30000),
    'Ford': ('green', 2019, 2.3, 'suv', 40000),
    'Chevrolet': ('purple', 2020, 1.4, 'hatchback', 22000),
    'Nissan': ('pink', 2018, 1.8, 'sedan', 35000),
    'Volkswagen': ('brown', 2021, 1.4, 'hatchback', 28000),
    'Hyundai': ('gray', 2019, 1.6, 'suv', 32000),
    'Kia': ('white', 2020, 2.0, 'sedan', 28000),
    'Volvo': ('silver', 2017, 1.8, 'suv', 45000),
    'Subaru': ('blue', 2018, 2.5, 'wagon', 35000),
    'Mazda': ('red', 2019, 2.5, 'sedan', 32000),
    'Porsche': ('black', 2017, 3.0, 'coupe', 80000),
    'Jeep': ('green', 2021, 3.0, 'suv', 50000),
    'Chrysler': ('gray', 2016, 2.4, 'sedan', 22000),
    'Dodge': ('yellow', 2020, 3.6, 'suv', 40000),
    'Ferrari': ('red', 2019, 4.0, 'coupe', 500000),
    'Lamborghini': ('orange', 2021, 5.0, 'coupe', 800000),
    'Maserati': ('blue', 2018, 4.7, 'coupe', 100000),
    'Bugatti': ('black', 2020, 8.0, 'coupe', 2000000),
    'McLaren': ('yellow', 2017, 4.0, 'coupe', 700000),
    'Rolls-Royce': ('white', 2019, 6.8, 'sedan', 500000),
    'Bentley': ('gray', 2020, 4.0, 'coupe', 300000),
    'Jaguar': ('red', 2016, 2.0, 'suv', 40000),
    'Land Rover': ('green', 2018, 3.0, 'suv', 60000),
    'Tesla': ('silver', 2020, 0.0, 'sedan', 60000),
    'Acura': ('white', 2017, 2.4, 'suv', 40000),
    'Cadillac': ('black', 2019, 3.6, 'suv', 55000),
    'Infiniti': ('gray', 2018, 2.0, 'sedan', 35000),
    'Lincoln': ('white', 2021, 2.0, 'suv', 50000),
    'GMC': ('blue', 2016, 1.5, 'pickup', 30000),
    'Ram': ('black', 2019, 5.7, 'pickup', 40000),
    'Chevy': ('red', 2017, 2.4, 'pickup', 35000),
    'Dodge Ram': ('white', 2020, 3.6, 'pickup', 45000),
    'Ford F-Series': ('gray', 2021, 3.5, 'pickup', 50000),
    'Nissan Titan': ('silver', 2018, 5.6, 'pickup', 35000),
}
info = (2017, 1.6, 36000)
"""


def find_cars_by_criteria(car_data, criteria):
    """
    Filter and retrieve cars from car_data that meet the search_criteria.

    Parameters:
    car_data (dict): A dictionary where the keys are
    car names and values are tuples containing
    (color, year, volume, type, price).
    criteria (tuple): A tuple containing criteria
    as (year_min, volume_min, price_max).
    - year_min (int): Minimum year the car should be.
    - volume_min (float): Minimum engine volume the car should have.
    - price_max (int): Maximum price the car should have.

    Returns:
    list: A list of up to 5 car names that match
    the criteria, sorted by price in ascending order.
    """
    year, volume, price = criteria

    # filter cars that meet the criteria
    matching_cars = [
        (name, details[4])
        for name, details in car_data.items()
        if details[1] >= year and details[2] >= volume and details[4] <= price
    ]

    # sort the filtered cars by price in ascending order
    matching_cars.sort(key=lambda car: car[1])

    # return up to 5 cars that meet the criteria
    return [name for name, _ in matching_cars[:5]]


# Example
car_data = {
    'Mercedes': ('silver', 2019, 1.8, 'sedan', 50000),
    'Audi': ('black', 2020, 2.0, 'sedan', 55000),
    'BMW': ('white', 2018, 3.0, 'suv', 70000),
    'Lexus': ('gray', 2016, 2.5, 'coupe', 45000),
    'Toyota': ('blue', 2021, 1.6, 'hatchback', 25000),
    'Honda': ('red', 2017, 1.5, 'sedan', 30000),
    'Ford': ('green', 2019, 2.3, 'suv', 40000),
    'Chevrolet': ('purple', 2020, 1.4, 'hatchback', 22000),
    'Nissan': ('pink', 2018, 1.8, 'sedan', 35000),
    'Volkswagen': ('brown', 2021, 1.4, 'hatchback', 28000),
    'Hyundai': ('gray', 2019, 1.6, 'suv', 32000),
    'Kia': ('white', 2020, 2.0, 'sedan', 28000),
    'Volvo': ('silver', 2017, 1.8, 'suv', 45000),
    'Subaru': ('blue', 2018, 2.5, 'wagon', 35000),
    'Mazda': ('red', 2019, 2.5, 'sedan', 32000),
    'Porsche': ('black', 2017, 3.0, 'coupe', 80000),
    'Jeep': ('green', 2021, 3.0, 'suv', 50000),
    'Chrysler': ('gray', 2016, 2.4, 'sedan', 22000),
    'Dodge': ('yellow', 2020, 3.6, 'suv', 40000),
    'Ferrari': ('red', 2019, 4.0, 'coupe', 500000),
    'Lamborghini': ('orange', 2021, 5.0, 'coupe', 800000),
    'Maserati': ('blue', 2018, 4.7, 'coupe', 100000),
    'Bugatti': ('black', 2020, 8.0, 'coupe', 2000000),
    'McLaren': ('yellow', 2017, 4.0, 'coupe', 700000),
    'Rolls-Royce': ('white', 2019, 6.8, 'sedan', 500000),
    'Bentley': ('gray', 2020, 4.0, 'coupe', 300000),
    'Jaguar': ('red', 2016, 2.0, 'suv', 40000),
    'Land Rover': ('green', 2018, 3.0, 'suv', 60000),
    'Tesla': ('silver', 2020, 0.0, 'sedan', 60000),
    'Acura': ('white', 2017, 2.4, 'suv', 40000),
    'Cadillac': ('black', 2019, 3.6, 'suv', 55000),
    'Infiniti': ('gray', 2018, 2.0, 'sedan', 35000),
    'Lincoln': ('white', 2021, 2.0, 'suv', 50000),
    'GMC': ('blue', 2016, 1.5, 'pickup', 30000),
    'Ram': ('black', 2019, 5.7, 'pickup', 40000),
    'Chevy': ('red', 2017, 2.4, 'pickup', 35000),
    'Dodge Ram': ('white', 2020, 3.6, 'pickup', 45000),
    'Ford F-Series': ('gray', 2021, 3.5, 'pickup', 50000),
    'Nissan Titan': ('silver', 2018, 5.6, 'pickup', 35000),
}
criteria = (2017, 1.6, 36000)


result = find_cars_by_criteria(car_data, criteria)
print(result)


# Task 9
"""Порахувати кількість унікальних символів в строці.
Якщо їх більше 10 - вивести в консоль True, інакше - False.
Строку отримати за допомогою функції input()
"""


def has_more_than_ten_unique_characters():
    """
    Count the number of unique characters in an input string.

    Prompts the user to enter a string and checks if
    it has more than 10 unique characters.

    Returns:
    bool: True if the number of unique characters is
    greater than 10, otherwise False.
    """
    user_input = input('Please enter some string: ')
    unique_characters = set(user_input)
    return len(unique_characters) > 10


print(has_more_than_ten_unique_characters())


# Task 10
"""
Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті
"""


def sum_of_even_numbers_in_range(start, end):
    """
    Calculate the sum of even numbers in a range.

    Parameters:
    start (int): The starting number of the range.
    end (int): The ending number of the range.

    Returns:
    int: The sum of all even numbers in the specified range.
    """
    numbers = list(range(start, end + 1))
    return sum(num for num in numbers if num % 2 == 0)


# Example
print(sum_of_even_numbers_in_range(1, 10))
