"""
Homework №2.

Tasks 01-10

"""

# task 01 == Виправте синтаксичні помилки
print('Hello', end = ' ')
print('world!')

# task 02 == Виправте синтаксичні помилки
hello = 'Hello'
world = 'world'
if True:
    print(f'{hello} {world}!')

# task 03  == Вcтавте пропущену змінну у ф-цію print
for letter in 'Hello world!':
    print(letter)

# task 04 == Зробіть так, щоб кількість бананів була
# завжди в чотири рази більша, ніж яблук
apples = 2
banana = apples * 4

# task 05 == виправте назви змінних
side_first = 1
side_second = 2
side_third = 3
side_fourth = 4

# task 06 == Порахуйте периметр фігури з task 05
# та виведіть його для користувача
perimeter = side_first + side_second + side_third + side_fourth
print(perimeter)


"""
    # Задачі 07 -10:
    # Переведіть задачі з книги "Математика, 2 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в другому класі
"""
# task 07
"""
У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
Скільки всього дерев посадили в саду?
"""

apples = 4
pears = apples + 5
plums = apples - 2
trees = apples + pears + plums
print(trees)

# task 08
"""
До обіда температура повітря була на 5 градусів вище нуля.
Після обіду температура опустилася на 10 градусів.
Надвечір потепліло на 4 градуси. Яка температура надвечір?
"""
morning_t = 5
midday_t = morning_t - 10
evening_t = midday_t + 4
print(evening_t)

# task 09
"""
Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
Скількі сьогодні дітей у театральному гуртку?
"""
theater_boys = 24
theater_girls = theater_boys / 2
sick_theater_boys = 1
absent_theater_girls = 2
today_theater_children = int(theater_boys + theater_girls - sick_theater_boys - absent_theater_girls)
print(today_theater_children)

# task 10
"""
Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
а третя - як половина вартості першої та другої разом.
Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
"""
book_one_price = 8
book_two_price = book_one_price + 2
book_three_price = (book_one_price + book_two_price) / 2
total_price = int(book_one_price + book_two_price + book_three_price)
print(total_price)
