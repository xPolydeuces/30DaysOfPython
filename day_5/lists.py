# Day 5: 30 Days of Python Programming

# LEVEL 1

from statistics import median


empty_list = []                                                                         # exercise 1

list_with_more_than_five_items = [2, 'car', 1.5, True, empty_list, {}]                  # exercise 2

print(len(list_with_more_than_five_items))                                              # exercise 3

print(list_with_more_than_five_items[0])                                                # exercise 4
print(list_with_more_than_five_items[-1])
print(list_with_more_than_five_items[len(list_with_more_than_five_items)//2])

mixed_data_types = ['Bart', 22, 183.3, False, 'Fake Street 1/9 00001 Fake City']        # exercise 5

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']  # exercise 6

print(it_companies)                                                                     # exercise 7

print("Number of companies in the list:",len(it_companies))                             # exercise 8

print(it_companies[0])                                                                  # exercise 9
print(it_companies[-1])
print(it_companies[len(it_companies)//2])

it_companies[4] = 'Lenovo'                                                              # exercise 10
print(it_companies)

it_companies.append('IBM')                                                              # exercise 11

it_companies.insert(len(it_companies)//2, 'Razer')                                      # exercise 12

it_companies[1] = it_companies[1].upper()                                               # exercise 13

it_companies_str = '#; '.join(it_companies)                                             # exercise 14

print('Lenovo' in it_companies)                                                         # exercise 15

it_companies.sort()                                                                     # exercise 16

it_companies.reverse()                                                                  # exercise 17
print(it_companies)

print(it_companies[3:])                                                                 # exercise 18

print(it_companies[:-3])                                                                # exercise 19

print(it_companies[:(len(it_companies)//2)]+it_companies[(len(it_companies)//2)+1:])    # exercise 20

it_companies.remove(it_companies[0])                                                    # exercise 21

it_companies.remove(it_companies[len(it_companies)//2])                                 # exercise 22

it_companies.remove(it_companies[-1])                                                   # exercise 23

it_companies.clear()                                                                    # exercise 24

it_companies = []                                                                       # exercise 25

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']                                     # exercise 26
back_end = ['Node','Express', 'MongoDB']
full_stack = front_end + back_end

full_stack.insert(full_stack.index('Redux'),'Python')                                   # exercise 27
full_stack.insert(full_stack.index('Redux'),'SQL')

# LEVEL 2

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
min_age = min(ages)
max_age = max(ages)
age_median = median(ages)
age_average = sum(ages)/len(ages)
age_range = max_age - min_age
print(abs((min_age - age_average)),abs((max_age - age_average)))

from countries import countries

print(countries[len(countries)//2])
first_half_countries, second_half_countries = countries[:len(countries)//2],countries[len(countries)//2:]
scandic_countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark'][3:]
print(scandic_countries)