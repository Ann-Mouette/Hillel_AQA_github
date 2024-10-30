"""
Homework №6.

Task 04.
"""

lst1 = list(range(20))
sum_of_evens = 0
for num in lst1:
    if num % 2 == 0:
        sum_of_evens += num
print(sum_of_evens)
