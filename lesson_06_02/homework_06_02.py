"""
Homework №6.

Task 02.
"""

user_str = input('Please enter a word with the letter "h": ')
while 'h' not in user_str.lower():
    print('Word should contain at least one "h" or "H". Please try again.')
    user_str = input('Please enter a word with the letter "h": ')
print('You are great!')
