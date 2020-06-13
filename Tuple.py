#Working with methods of Tuple:
#Tuples are Immutable so we can't do updation methods on Tuple.

numbers = (25, 36, 49, 64, 81, 100, 121)         # Creating a numbers tuple
print("The tuple of numbers : ",numbers)

count = numbers.count(25)                   # count() count how many times mentioned element is occured in Tuple
print("\nThe occurence of 25 in the numbers tuple is: ", count)

index = numbers.index(36)                   # index() gives us index of mentioned element in Tuple
print("\nThe index of 36 is: ",index)

length = len(numbers)                       # len() is used to extract length of Tuple
print("\nThe length of the numbers tuple is: ", length)

Max_number = max(numbers)                   # max() gives result as Largest element from Tuple
print("\nThe maximum number of the numbers tuple is: ", Max_number)

Min_number = min(numbers)                   # min() gives result as smallest element from Tuple
print("\nThe minimum number of the numbers tuple is: ", Min_number)

Sum =sum (numbers)                          # sum() gives result as sum of elements in Tuple
print("\nThe sum of all elements in the tuple numbers is: ", Sum)

list = [1, 11, 111, 1111]
Tuple = tuple(list)                         # We can apply casting like this to convert list into Tuple
print("\nThe tuple obtained by converting a list into tuple is: ", Tuple)
