"""
Homework №3.

Tasks 01-10.
"""
import math

alice_in_wonderland = ('"Would you tell me, please, which way I '
                       'ought to go from here?"\n'
                       '"That depends a good deal on where you want '
                       'to get to," said the Cat.\n'
                       '"I don\'t much care where '
                       '——" said Alice."\n'
                       '"Then it doesn\'t matter which way you '
                       'go," said the Cat.\n'
                       '"—— so long as I get somewhere," Alice '
                       'added as an explanation.\n'
                       '"Oh, you\'re sure to do that," said '
                       'the Cat, "if you only walk long enough."')
print(alice_in_wonderland)

# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала
# декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк


"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
black_sea_area = 436402
azov_sea_area = 37800
combined_sea_area = black_sea_area + azov_sea_area
print(combined_sea_area, 'km')

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
all_stock = 375291
first_stock = (all_stock - 222950)
third_stock = (all_stock - 250449)
second_stock = all_stock - (first_stock + third_stock)
print(str(first_stock) + ', ' + str(second_stock) + ', ' + str(third_stock))


# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
laptop_cost = (12 + 12 / 2) * 1179
print(laptop_cost, 'uah')

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
print(8019 % 8)
print(9907 % 9)
print(2789 % 5)
print(7248 % 6)
print(7128 % 5)
print(19224 % 9)

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
pizza_big = 4 * 274
pizza_middle = 2 * 218
juice = 4 * 35
cake = 1 * 350
water = 3 * 21
total_cost = pizza_big + pizza_middle + juice + cake + water
print(total_cost, 'uah')

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
pages_for_photo = 232 / 8
print(pages_for_photo)

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
petrol_for_trip = 1600 / 100 * 9
km_for_tank = (48 / 9) * 100
stops = 1600 / km_for_tank
stops = math.ceil(stops)
print('Petrol for trip:', petrol_for_trip, 'L, ' 'refueling stops:', stops)
