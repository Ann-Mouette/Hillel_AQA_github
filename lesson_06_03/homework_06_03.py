"""
Homework №6.

Task 03.
"""
lst1 = ['1', '2', 3, True, 'False', 5, '6', 8, 'Python', 9, 0, 'Lorem Ipsum']
lst2 = []
for i in lst1:
    if type(i) is str:
        lst2.append(i)
print(lst2)
