"""
Homework №07_01.

Tasks 1-10
"""

# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1
    while True:
        result = number * multiplier
        if  result > 25:
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))
        multiplier += 1

multiplication_table(3)


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def count_sum(a, b):
    res = a + b
    print('Result:', res)


count_sum(3,2)

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def count_average(numbers):
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
    return text[::-1]


# Example:
text = "Hello"
print(reverse_string(text))

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def find_longest_words(words):
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
words = ["apple", "acer", "htc", "nokia"]
print(find_longest_words(words))

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(string_main, substring):
    return string_main.find(substring)

string_main = "I like broccoli and cilantro!"
substring = "broccoli"
print(find_substring(string_main, substring)) #return: 7

str1 = "Lorem ipsum dolor sit amet, consectetur adipiscing"
str2 = "Fusce quis"
print(find_substring(str1, str2)) #return: -1

# task 7
# task 8
# task 9
# task 10
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""

# task 7
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
def calculate_goods_per_stock(all_stock, stock_1_2, stock_2_3):
    """
    Calculates the number of goods in each of the warehouses.

    Parameters:
    all_stock (int): The total number of goods in three warehouses.
    stock_1_2 (int): The number of goods in the first and second warehouses together.
    stock_2_3 (int): The number of goods in the second and third warehouses together.

    Returns:
    dict: dictionary with the number of goods in each warehouse (keys: 'stock one', 'stock two', 'stock three').
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
        'stock three': stock_3
    }


# Example
all_stock = 375291
stock_1_2 = 250449
stock_2_3 = 222950

result = calculate_goods_per_stock(all_stock, stock_1_2, stock_2_3)
print(result)