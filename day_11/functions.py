# Day 11: 30 Days of Python Programming

# LEVEL 1

import math


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
