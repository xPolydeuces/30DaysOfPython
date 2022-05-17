# Day 8: 30 Days of Python Programming

dog = {}                                                    # exercise 1

dog['name'] = 'Puppy'                                       # exercise 2
dog['color'] = 'white'
dog['legs'] = 4
dog['age'] = 5

student = {                                                 # exercise 3
    'first_name': 'John',
    'last_name': 'Doe',
    'gender': 'Male',
    'age': 25,
    'marital_status': False,
    'skills': ['cooking', 'coding', 'volleyball', 'napping'],
    'country': 'United States of Cool',
    'city': 'Cool City',
    'address': 'Kul Street 13/37'
    }

print(len(student))                                         # exercise 4

print(student['skills'])                                    # exercise 5
print(type(student['skills']))

student['skills'].append('gaming')                          # exercise 6

print(student.keys())                                       # exercise 7

print(student.values())                                     # exercise 8

print(student.items())                                      # exercise 9

del student['marital_status']                               # exercise 10

del student                                                 # exercise 11