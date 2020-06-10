#Python File with basic Numerical calculations

# Arthmetic

print(27 + 5)  # This Addition results 32
print(27 - 5)  # This Subtraction results 22
print(27 * 5)  # This Multiplication results 135
print(27 / 5)  # This Division results 5.4
print(27 % 5)  # This results 2 as remainder of 27 divided by 5

# Following are special operations in python on numbers
print(27 // 5)  # "//" gives integer results 5 from float result of 27 divided by 5
print(27 ** 5)  # "**" gives answer 14348907 as result of 5 times power of 27

# Comparative, Boolean
print(27 == 5)  # Result : False
print(27 != 5)  # Result : True
print(27 <= 5)  # Result : False
print(27 >= 5)  # Result : True
print(27 < 5)  # Result : False
print(27 > 5)  # Result : True

# Numericals using variables

int1 = 27
int2 = 5

print(int1 + int2)  # Result : 32

# Casting Numbers

int1 = '27'
int2 = '5'

print(int1 + int2)  # Gives result as "275" because integers are being assumed as string and so concatenation occured

# If we want proper numeric answer of above calculation we have use Casting Number method

int1 = "27"
int2 = "5"

int1 = int(int1)
int2 = int(int2)

print(int1 + int2)  # Now here after casting int1 and int2 we get 32 as result in numeric values
