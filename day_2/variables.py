# Day 2: 30 Days of Python Programming

# LEVEL 1

first_name = "John"                         # str
last_name = "Doe"                           # str
full_name = first_name + ' ' + last_name    # str
country = "United States of America"        # str
city = "New York"                           # str
age = 25                                    # int
year = 2022                                 # int
is_married = False                          # bool
is_true = True                              # bool
is_light_on = True                          # bool
x, y, z = 1.5, 2j, 30                       # float, complex, int

# LEVEL 2

print(type(first_name))                     # str
print(type(last_name))                      # str
print(type(full_name))                      # str
print(type(country))                        # str
print(type(city))                           # str
print(type(age))                            # int
print(type(year))                           # int
print(type(is_married))                     # bool
print(type(is_true))                        # bool
print(type(is_light_on))                    # bool
print(type(x))                              # float
print(type(y))                              # complex
print(type(z))                              # int

print(f"Lenght of the first name: {len(first_name)}")
print(f"Is first name longer than last name?\nAnswer: {len(first_name) > len(last_name)}")

num_one = 5
num_two = 4
total = num_one + num_two                   # 9
diff = num_two - num_one                    # 1
product = num_two * num_one                 # 20
division = num_one / num_two                # 1.25
remainder = num_two % num_one               # 4
exp = num_one ** num_two                    # 625
floor_division = num_one // num_two         # 1


PI = 3.1416
r = 30


def area_circle(r):
    '''Function takes radius of a circle and returns its area'''
    return PI * r ** 2


area_of_circle = area_circle(r)             # ≈ 2827.44
circum_of_circle = 2 * PI * r               # ≈ 188.496

user_r = int(input("Radius: "))
print(area_circle(user_r))

first_name = input("First name: ")
last_name = input("Last name: ")
country = input("Country: ")
age = int(input("Age: "))

help('keywords')