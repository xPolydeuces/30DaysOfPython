# LEVEL 2

# Check the version
from sys import version

print(f"Python version: {version}")

# Operations on numbers

print(f"2 + 8 =", 2+8)          # addition
print(f"23 - 15 =", 23-15)      # subtraction
print(f"76 * 22 =", 76*22)      # multiplication
print(f"4 % 6 =", 4%6)          # modulo
print(f"55 / 11 =", 55/11)      # division
print(f"2^12 =", 2**12)         # exponential
print(f"3 // 2 =", 3//2)        # floor division

# Writing strings

print("Bartosz", end=' ')
print("Kot")
print("Poland")
print("I am enjoying 30 days of Python")

# Checking data types

print(type(10))                                 # int
print(type(9.8))                                # float
print(type(3.14))                               # float
print(type(4 - 4j))                             # complex
print(type(['Asabeneh', 'Python', 'Finland']))  # list
print(type("Bartosz"))                          # str
print(type("Kot"))                              # str
print(type("Poland"))                           # str


# LEVEL 3

print(type(123))                                # int
print(type(1.5))                                # float
print(type(3 + 2j))                             # complex
print(type("Hello World!"))                     # str
print(type(True))                               # boolean
print(type([1, 2, 3]))                          # list
print(type((1, 2, 3)))                          # tuple
print(type({1, 2, 3}))                          # set
print(type({'1': 1, '2': 2, '3': 3}))           # dict

from math import sqrt

print("Euclidean Distance between (2, 3) and (10, 8) is ", sqrt((2 - 10)**2 + (3 - 8)**2))