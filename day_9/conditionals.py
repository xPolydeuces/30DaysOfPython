# Day 9: 30 Days of Python Programming

def can_drive():                                                                        # exercise 1
    user_input = int(input("Enter your age: "))
    if user_input >= 18:
        return "You are old enough to drive."
    else:
        return f"You need {18 - user_input} more years to learn to drive."

#print(can_drive())

def compare_age():                                                                      # exercise 2
    my_age = 25
    user_input = int(input("Enter your age: "))
    if my_age > user_input:
        return f"You are {my_age - user_input} years younger than me."
    if my_age == user_input:
        return "Wow, we are the same age!"
    if my_age < user_input:
        return f"You are {user_input - my_age} years older than me."

#print(compare_age())

def compare_numbers():                                                                  # exercise 3
    num1 = int(input("Enter number one: "))
    num2 = int(input("Enter number two: "))
    if num1 > num2:
        return f"{num1} is greater than {num2}"
    if num1 == num2:
        return f"{num1} is equal to {num2}"
    if num1 < num2:
        return f"{num1} is smaller than {num2}"

#print(compare_numbers())

# LEVEL 2

def grade_students(grade: int):                                                         # exercise 1
    if grade >= 90:
        return 'A'
    if grade >= 70:
        return 'B'
    if grade >= 60:
        return 'C'
    if grade >= 50:
        return 'D'
    else:
        return 'F'

#print(grade_students(80))

def seasons():                                                                          # exercise 2
    spring = ['march', 'april', 'may']
    summer = ['june', 'july', 'august']
    autumn = ['september', 'october', 'november']
    winter = ['december', 'january', 'february']
    user_input = input("What is the current month? \n>: ")
    if user_input.lower() in spring:
        return 'Spring'
    if user_input.lower() in summer:
        return 'Summer'
    if user_input.lower() in autumn:
        return 'Autumn'
    if user_input.lower() in winter:
        return 'Winter'
    else:
        return 'Wrong input!'

#print(seasons())

def fruits_func():                                                                       # exercise 3
    fruits = ['banana', 'orange', 'mango', 'lemon']
    user_input = input("Enter name of any fruit you want: ")
    if user_input.lower() in fruits:
        return 'That fruit already exists in the list'
    fruits.append(user_input)
    return fruits

#print(fruits_func())

# LEVEL 3

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

if 'skills' in person.keys():
    print(person['skills'][len(person['skills'])//2])                           # exercise 1
    if 'Python' in person['skills']:                                            # exercise 2
        print("There is 'Python' in 'skills' list.")
    else:
        print("There is no 'Python' in 'skills' list.")
    if 'JavaScript' in person['skills'] and 'React' in person['skills']:        # exercise 3
        print("He is a front end developer.")
    if 'Node' in person['skills'] and 'Python' in person['skills'] and 'MongoDB' in person['skills']:
        print("He is a back end developer.")
    if 'Node' in person['skills'] and 'React' in person['skills'] and 'MongoDB' in person['skills']:
        print("He is a full-stack developer.")
    else:
        print("Unknown title.")

if person['is_married'] == True and person['country'] == 'Finland':             # exercise 4
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.")
