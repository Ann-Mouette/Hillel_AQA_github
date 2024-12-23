"""
My little SQLAlchemy.

1. Створення моделі даних: Створіть просту модель даних для системи управління
студентами. Модель може містити таблиці для студентів, курсів та їх відношень.
Кожен студент може бути зареєстрований на декілька курсів. Наприклад, створити
5 курсів, та розподілити рандомно 20 студентів.

2. Виконання базових операцій: Напишіть програму, яка додає нового студента до
бази даних та додає його до певного курсу. Переконайтеся, що ці зміни коректно
відображаються у базі даних.

3. Запити до бази даних: Напишіть запити до бази даних, які повертають
інформацію про студентів, зареєстрованих на певний курс, або курси, на які
зареєстрований певний студент.

4. Оновлення та видалення даних: Реалізуйте можливість оновлення даних про
студентів або курси, а також видалення студентів з бази даних.

5. Можна використовувати будь-яку ORM на ваш вибір.
"""

import random

from sqlalchemy import (Column, ForeignKey, Integer, String, Table,
                        create_engine)
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()

student_course_association = Table(
    'student_course',
    Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id')),
    Column('course_id', Integer, ForeignKey('courses.id')),
)


class Student(Base):
    """Model for Student."""

    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    courses = relationship(
        'Course',
        secondary=student_course_association,
        back_populates='students',
    )

    def __repr__(self):
        """Represent string of a Student instance."""
        return f'<Student(id={self.id}, name="{self.name}")>'


class Course(Base):
    """Model for Course."""

    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)

    students = relationship(
        'Student',
        secondary=student_course_association,
        back_populates='courses',
    )

    def __repr__(self):
        """Represent string of a Course instance."""
        return f'<Course(id={self.id}, title="{self.title}")>'


engine = create_engine('sqlite:///student_management.db', echo=False)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


def create_courses():
    """Create and add 5 courses to the database."""
    courses = [
        Course(title='Math'),
        Course(title='Physics'),
        Course(title='Chemistry'),
        Course(title='Biology'),
        Course(title='History'),
    ]
    session.add_all(courses)
    session.commit()
    print('Courses created:', courses)


def create_students():
    """Create 20 students and randomly assign them to courses."""
    courses = session.query(Course).all()
    students = []

    for i in range(1, 21):
        student = Student(name=f'Student {i}')
        student.courses = random.sample(courses, random.randint(1, 3))
        students.append(student)

    session.add_all(students)
    session.commit()
    print('Students created and assigned to courses:', students)


def add_student(name, course_title):
    """Add a new student and register them for a specific course."""
    course = session.query(Course).filter_by(title=course_title).first()
    if not course:
        print(f'Course "{course_title}" not found.')
        return

    new_student = Student(name=name)
    new_student.courses.append(course)
    session.add(new_student)
    session.commit()
    print(f'Added {new_student} to course "{course_title}".')


def get_students_in_course(course_title):
    """Get all students registered in a specific course."""
    course = session.query(Course).filter_by(title=course_title).first()
    if not course:
        print(f'Course "{course_title}" not found.')
        return

    print(f'Students in course "{course_title}":', course.students)


def get_courses_for_student(student_name):
    """Get all courses a specific student is registered in."""
    student = session.query(Student).filter_by(name=student_name).first()
    if not student:
        print(f'Student "{student_name}" not found.')
        return

    print(f'Courses for student "{student_name}":', student.courses)


def update_student_name(old_name, new_name):
    """Update a student's name."""
    student = session.query(Student).filter_by(name=old_name).first()
    if not student:
        print(f'Student "{old_name}" not found.')
        return

    student.name = new_name
    session.commit()
    print(f'Updated student name from "{old_name}" to "{new_name}".')


def delete_student(name):
    """Delete a student from the database."""
    student = session.query(Student).filter_by(name=name).first()
    if not student:
        print(f'Student "{name}" not found.')
        return

    session.delete(student)
    session.commit()
    print(f'Deleted student "{name}" from the database.')


if __name__ == '__main__':
    create_courses()
    create_students()

    add_student('New Student', 'Math')
    get_students_in_course('Math')
    get_courses_for_student('Student 1')

    update_student_name('Student 1', 'Updated Student 1')
    delete_student('Student 2')
