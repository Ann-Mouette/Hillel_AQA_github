"""
Homework №8.

Task 01.
"""
# Створіть масив зі строками, які будуть складатися з чисел,
# які розділені комою. Наприклад:
# [”1,2,3,4”, ”1,2,3,4,50” ”qwerty1,2,3”]
# Для кожного елементу списку виведіть суму всіх чисел
# (створіть нову функцію для цього).
# Якщо є символи, що не є числами (”qwerty1,2,3” у прикладі),
# вам потрібно зловити вийняток і вивести “Не можу це зробити!”
# Використовуйте блок try\except, щоб уникнути інших символів,
# окрім чисел у списку.
# Для цього прикладу правильний вивід буде - 10, 60,
# “Не можу це зробити”


def calc_sum_of_numbers_in_str(num_string):
    """
    Calculate the sum of numbers in a comma-separated string.

    Parameters:
    num_string (str): A string containing numbers separated by commas.

    Returns:
    int or str: The sum of numbers if successful,
    or an error message if the string contains non-numeric characters.
    """
    try:
        numbers = [int(num) for num in num_string.split(',')]
        return sum(numbers)
    except ValueError:
        return 'Не можу це зробити!'


strings = ['6,7,8,9', '15,85,34,50', 'random3,2,1']
results = [calc_sum_of_numbers_in_str(num_string) for num_string in strings]


for result in results:
    print(result)
