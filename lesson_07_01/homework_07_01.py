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


# Example usage:
numbers = [1, 2, 3, 4, 5]
print(count_average(numbers))

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def reverse_string(text):
    return text[::-1]



# Example usage:
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
            longest_words = [word]  # Починаємо новий список із цього слова
        elif len(word) == max_length:
            longest_words.append(word)  # Додаємо слово, якщо його довжина дорівнює max_length

    return longest_words


# Example usage:
words = ["яблуко", "банан", "грушка", "кавун"]
print(find_longest_words(words))

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):

    return -1

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7
# task 8
# task 9
# task 10
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""