"""
Homework №12 (lesson 14).

Створіть клас "Студент" з атрибутами "ім'я", "прізвище",
"вік" та "середній бал". Створіть об'єкт цього класу,
представляючий студента. Потім додайте метод до класу "Студент",
який дозволяє змінювати середній бал студента. Виведіть
інформацію про студента та змініть його середній бал.
"""


class Student:
    """This class represents a student with attributes."""

    def __init__(self, name, surname, age, average_score):
        """Initialize a student with the given attributes."""
        self.name = name
        self.surname = surname
        self.age = age
        self.average_score = average_score

        print(
            f'Created student: {self.name} {self.surname}, age: {self.age}, '
            f'average score: {self.average_score}.',
        )

    def change_average_score(self, new_score):
        """Change the average score of the student."""
        self.average_score = new_score
        print(
            f'The average score of {self.name} {self.surname} changed to '
            f'{self.average_score}.',
        )


st1 = Student('Anna', 'Chaika', 41, 80)

st1.change_average_score(100)
