"""
Homework №9.

Task 01.

we have two lists with equal or different size
ex. l1=[1,3,5,7]  l2=[1,4,5]
task:
create list that will store such values
ex. list_target = [(1,1), (3,4), (5,5), (7,0)]
zero (0) is our default value that we set if no such
element by index was found in certain list.
code should work and vise versa
ex. l1=[1,4,5] l2=[1,3,5,7] input data should produce
ex. list_target = [(1,1), (4,3), (5,5), (0,7)]
your solution should include comprehension constructions
Advices:
set of (list1 indexes union list2 indexes) could be helpful
to get larger indexes scope ( or use if-else)
dict as you remember has default value if key was not found
ex. d1.get(key, 0)
"""


def merge_lists(list1, list2):
    """
    Merge two lists.

    Parameters:
    list1 (list): The first list of elements.
    list2 (list): The second list of elements.

    Returns:
    list: A list of tuples, where each tuple contains a pair of elements
    from list1 and list2 at the same index. If one list is shorter,
    0 is used as the default for the missing values.
    """
    d1 = {i: list1[i] for i in range(len(list1))}
    d2 = {i: list2[i] for i in range(len(list2))}

    all_indices = set(d1.keys()).union(d2.keys())

    list_target = [(d1.get(i, 0), d2.get(i, 0)) for i in sorted(all_indices)]

    return list_target


# Example 1
user_list1 = [1, 4, 5]
user_list2 = [1, 3, 5, 7]
print(merge_lists(user_list1, user_list2))

# Example 2
user_list1 = [2, 4, 6, 8, 10]
user_list2 = [1, 2, 3]
print(merge_lists(user_list1, user_list2))
