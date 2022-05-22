# Day 11: 30 Days of Python Programming

# LEVEL 1

import math
from string import digits


def add_two_numbers(a,b):
    '''Exercise 1'''
    return a + b

def area_of_circle(r):
    '''Exercise 2'''
    return 3.14 * (r ** 2)

def add_all_nums(*nums):
    '''Exercise 3'''
    return sum(nums) if all(isinstance(num, (int, float))for num in nums) else "All nums must be numbers!"

def convert_celcius_to_fahrenheit(celcius):
    '''Exercise 4'''
    return celcius * (9/5) + 32

def check_season(month):
    '''Exercise 5'''
    seasons = {
        'Spring':['March', 'April', 'May'],
        'Summer':['June', 'July', 'August'],
        'Autumn':['September', 'October', 'November'],
        'Winter':['December', 'January', 'February']
    }
    return [key for key, value in seasons.items() if month in value][0]

def calculate_slope(x1,y1,x2,y2):
    '''Exercise 6'''
    return (y2-y1)/(x2-x1)

def solve_quadratic_eqn(a,b,c):
    '''Exercise 7'''
    if a == 0:
        return "a can't be equal 0!"
    d = (b**2) - (4*a*c)
    if d > 0:
        sol1 = (-b-math.sqrt(d))/(2*a)
        sol2 = (-b+math.sqrt(d))/(2*a)
        return f"The solutions are x1 = ({sol1}) and x2 = ({sol2})"
    if d == 0:
        return f"The solution is x = ({-b/(2*a)})"
    if d < 0:
        return f"There are no solutions."

def print_list(lst:list):
    '''Exercise 8'''
    for element in lst:
        print(element)

def capitalize_list_items(lst:list):
    '''Exercise 10'''
    return [i.capitalize() for i in lst]

def add_item(lst:list, item):
    '''Exercise 11'''
    lst.append(item)
    return lst

def remove_item(lst:list, item):
    '''Exercise 12'''
    lst.remove(item)
    return lst

def sum_of_numbers(num:int):
    '''Exercise 13'''
    return sum([i for i in range(num+1)])

def sum_of_odds(num:int):
    '''Exercise 14'''
    return sum([i for i in range(num+1) if i % 2 != 0])

def sum_of_evens(num:int):
    '''Exercise 15'''
    return sum([i for i in range(num+1) if i % 2 == 0])

# LEVEL 2

def evens_and_odds(num:int):
    '''Exercise 1'''
    if num < 1:
        return "Number must be positive!"
    evens = len([i for i in range(num+1) if i % 2 == 0])
    odds = len([i for i in range(num+1) if i % 2 != 0])
    return f"The number of evens is {evens} and of odds is {odds}."

def factorial(num:int):
    '''Exercise 2'''
    fct = 1
    for i in range(1,num+1):
        fct *= i
    return fct

def is_empty(parameter):
    '''Exercise 3'''
    return True if len(parameter) == 0 else False

# LEVEL 3

def is_prime(num):
    '''Exercise 1'''
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

def is_unique(lst:list):
    '''Exercise 2'''
    tmp_lst = []
    for item in lst:
        if item in tmp_lst:
            return False
        tmp_lst.append(item)
    return True

def same_type(lst:list):
    '''Exercise 3'''
    prev = lst[0]
    for i in lst:
        if type(i) != type(prev):
            return False
        prev = i
    return True

import keyword
def valid_variable(var):
    '''Exercise 4'''
    digits
    if var in keyword.kwlist:
        return False
    if var[0] in digits:
        return False
    return True

