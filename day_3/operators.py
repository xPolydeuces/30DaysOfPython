# Day 3: 30 Days of Python Programming
from math import sqrt

my_age = 22                                                                                 # exercise 1
my_height = 183.5                                                                           # exercise 2
complex_number = 1j                                                                         # exercise 3

def triangle_area(b, h):                                                                    # exercise 4
    '''Function takes base and height arguments and returns area of the triangle'''
    return 0.5 * b * h

def triangle_perimeter(a, b, c):                                                            # exercise 5
    '''Function takes sides a, b and c arguments and returns perimeter of the triangle'''
    return a + b + c

def rectangle_area(l,w):                                                                    # exercise 6
    '''Function takes lenght and width arguments and returns area of the rectangle'''
    return l * w

def rectangle_perimeter(l,w):
    '''Function takes lenght and width arguments and returns perimeter of the rectangle'''
    return 2 * (l+w)

def circle_area(r):                                                                         # exercise 7
    '''Function takes radius argument and returns area of the circle'''
    return PI * r ** 2

def circle_circumference(r):
    '''Function takes radius argument and returns circumference of the circle'''
    return 2 * PI * r

base = int(input("Enter base: "))
height = int(input("Enter height: "))
print("The area of the triangle is",triangle_area(base,height))

a = int(input("Enter side a: "))
b = int(input("Enter side b: "))
c = int(input("Enter side c: "))
print("The perimeter of the triangle is",triangle_perimeter(a,b,c))

lenght = int(input("Enter lenght: "))
width = int(input("Enter width: "))
print("The area of the rectangle is",rectangle_area(lenght,width))
print("The perimeter of the rectangle is",rectangle_perimeter(lenght,width))

PI = 3.1416
radius = int(input("Enter radius: "))
print("The area of the circle is",circle_area(radius))
print("The circumference of the circle is",circle_circumference(radius))

def x_intercept():                                                                              # exercise 8
    '''Function returns x-intercept of y = 2x - 2'''
    y = 0
    return (2/2-y,y)

def y_intercept():
    '''Function returns y-intercept of y = 2x - 2'''
    x = 0
    return (x, 2*x-2)

def slope(x1,y1,x2,y2):
    '''Function returns slope'''
    return (y2-y1)/(x2-x1)

def euclidean(x1,y1,x2,y2):
    '''Function returns Euclidean distance'''
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)

x = x_intercept()                                                           # (1.0, 0)
y = y_intercept()                                                           # (0, -2)
slope_result1 = slope(x[0],x[1],y[0],y[1])                                   # 2.0
print(f"For x-intercept {x} and y-intercept {y} slope is {slope_result1}.")

x = (2, 2)                                                                                      # exercise 9
y = (6,10)
slope_result2 = slope(x[0],x[1],y[0],y[1])
eucli_result = euclidean(x[0],x[1],y[0],y[1])
print(f"For point x being {x} and for point y being {y}, slope is {slope_result2} and Euclidean distance is {eucli_result}.")
print(f"Is first slope ({slope_result1}) the same as second slope ({slope_result2})?", slope_result1 == slope_result2)      # exercise 10

def value_of_y(x):                                                                              # exercise 11
    '''Calculates value of y for y = x^2 + 6x + 9'''
    return x**2 + 6*x + 9

x = int(input("Enter x: "))
y = value_of_y(x)
print(f"y for x = {x} is {y}")

python, dragon = 'python', 'dragon'                                                             # exercise 12
print(f"'python' length is {len(python)}, while 'dragon' length is {len(dragon)}. Therefore, they are not the same length.", len(python) != len(dragon))
print('on' in python and 'on' in dragon)                                                        # exercise 13
sentence = "I hope this course is not full of jargon."                                          # exercise 14
print('jargon' in sentence)
print('on' not in python and 'on' not in dragon)                                                # exercise 15
print(str(float(len(python))))                                                                  # exercise 16

def is_even(num):                                                                               # exercise 17
    return num % 2 == 0

print(is_even(5))
print(is_even(20))
print(7//3 == int(2.7))                                                                         # exercise 18
print(type(10) == type('10'))                                                                   # exercise 19
print(int(9.8) == 10)                                                                           # exercise 20

def pay(hours, rate):                                                                           # exercise 21
    '''Function takes hours and rate arguments and returns your pay'''
    return hours * rate

hours = int(input("Enter hours: "))
rate = int(input("Enter rate per hour: "))
print("Your weekly earning is",pay(hours,rate))

def years_to_seconds(years):                                                                    # exercise 22
    '''Function takes years as an argument and returns it in seconds, unless you are older than 100'''
    if years > 100:
        return "You are dead! Not big surprise."
    return years * 365*  24 * 60 * 60

years = int(input("Enter number of years you have lived: "))
print(f"You have lived for {years_to_seconds(years)} seconds.")

for i in range(1,6):                                                                            # exercise 23
    print(i, i**0, i**1, i**2, i**3)