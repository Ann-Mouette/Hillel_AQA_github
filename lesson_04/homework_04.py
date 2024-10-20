"""
Homework №4.

Tasks 1-10.
"""

adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled
his legs, munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy
Fisher for a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

# ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через
помилку. треба замінити кінець абзацу на пробіл .replace("\n", " ")"""

adwentures_of_tom_sawer1 = adwentures_of_tom_sawer.replace('\n', ' ')
print(adwentures_of_tom_sawer1)

# task 02 ==
""" Замініть .... на пробіл
"""
adwentures_of_tom_sawer2 = adwentures_of_tom_sawer1.replace('....', ' ')
print(adwentures_of_tom_sawer2)

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
adwentures_of_tom_sawer3 = ' '.join(adwentures_of_tom_sawer2.split())
print(adwentures_of_tom_sawer3)

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
adwentures_of_tom_sawer_h = adwentures_of_tom_sawer3.count('h')
print(adwentures_of_tom_sawer_h)

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
list_of_words = adwentures_of_tom_sawer3.split()
capitalized_count = 0
for word in list_of_words:
    if word[0].isupper():
        capitalized_count += 1
print(capitalized_count)

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
first_tom = adwentures_of_tom_sawer3.find('Tom')
print(adwentures_of_tom_sawer3.find('Tom', first_tom + 1))

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer3.split('. ')
print(adwentures_of_tom_sawer_sentences)

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
print(f'{adwentures_of_tom_sawer_sentences[3].lower()}.')

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
for sentence in adwentures_of_tom_sawer_sentences:
    if sentence.startswith('By the time'):
        print(f'Речення, яке починається з "By the time": {sentence}')

# task 10
""" Виведіть кількість слів останнього речення з
adwentures_of_tom_sawer_sentences.
"""
last_sentence = adwentures_of_tom_sawer_sentences[-1]
words_in_last_sentence = last_sentence.split()
print(len(words_in_last_sentence))
