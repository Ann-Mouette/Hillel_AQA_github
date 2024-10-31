"""
Homework №6.

Task 01.
"""
user_str = input('Please enter smth: ')
if len(set(user_str)) > 10:
    print('True')
else:
    print('False')
