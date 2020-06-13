# Working with methods of Lists:
# List are ordered so we can use indexing methods on list
numbers = [25, 36, 49, 64, 81, 100, 121]      # creating a numbers list:
print("The list of numbers : ", numbers)

numbers.append(144)      # append() adds element in list at last position
print("\nThe list of numbers after using appending 144: ", numbers)

numbers.insert(2, 16)   # By insert() we can adds element in list at specific index position
print("\nThe list of numbers after using inserting 16 at 2nd Index: ", numbers)

numbers.remove(36)      # remove() removes mentioned element in list
print("\nThe list of numbers after using removing 36: ", numbers)

numbers.pop(4)          # pop() removes element in list from mentioned index position
print("\nThe list of numbers after using pop method for index 4: ", numbers)

numbers.pop()           # pop() removes element in list from last position
print("\nThe list of numbers after using pop method without index: ", numbers)

numbers.extend([1, 4, 9])       # we can use extend() to add more than one element at a time
print("\nThe list of numbers after using extend for elements (1,4,9): ", numbers)

numbers.sort()      # sort() used to sort list
print("\nThe Sorted list of numbers after sorting: ", numbers)

Min_numbers = min(numbers)      # min() is used to find smallest element from list
print("\nThe minimum number from the list numbers is: ", Min_numbers)

Max_numbers = max(numbers)      # max() is used to find Largest element from list
print("\nThe maximum number from the list numbers is: ", Max_numbers)

Sum_numbers = sum(numbers)      # sum() is used to find Sum of elements in list
print("\nThe sum of all elements in the list numbers is: ", Sum_numbers)

del numbers[:2]                 # del listname[:] is used to delete multiple elements from list
print("\nList after deleting elements till 2nd Index: ", numbers)
