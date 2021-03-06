# Day 4: 30 Days of Python Programming

thirty_days_str = 'Thirty' + ' ' + 'Days' + ' ' + 'Of' + ' ' + 'Python'             # exercise 1

coding_str = 'Coding' + ' ' + 'For' + ' ' + 'All'                                   # exercise 2

company = coding_str                                                                # exercise 3

print(company)                                                                      # exercise 4

print(len(company))                                                                 # exercise 5

print(company.upper())                                                              # exercise 6

print(company.lower())                                                              # exercise 7

print(company.capitalize())                                                         # exercise 8
print(company.title())
print(company.swapcase())

no_coding_str = coding_str[7:]                                                      # exercise 9

print(no_coding_str.find('Coding'))                                                 # exercise 10

print(coding_str.replace('Coding','Python'))                                        # exercise 11

python_for_everyone = "Python for Everyone"                                         # exercise 12
print(python_for_everyone.replace('Everyone', 'All'))

coding_split = coding_str.split(' ')                                                # exercise 13

companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"               # exercise 14
companies_split = companies.split(',')

print(coding_str[0])                                                                # exercise 15

print(coding_str.rindex(coding_str[-1]))                                            # exercise 16

print(coding_str[10])                                                               # exercise 17

python_for_acronym = [letter[0].upper() for letter in python_for_everyone.split()]  # exercise 18
print(''.join(python_for_acronym))

coding_acronym = [letter[0].upper() for letter in coding_str.split()]               # exercise 19
print(''.join(coding_acronym))

print(coding_str.index('C'))                                                        # exercise 20

print(coding_str.index('F'))                                                        # exercise 21

print(coding_str.rfind('l'))                                                        # exercise 22

print('You cannot end a sentence with because because because is a conjunction'.index('because'))       # exercise 23

print('You cannot end a sentence with because because because is a conjunction'.rindex('because'))      # exercise 24

print('You cannot end a sentence with because because because is a conjunction'[31:54])                 # exercise 25

print('Coding' in coding_str)                                                       # exercise 28

print('coding' in coding_str)                                                       # exercise 29

print('   Coding For All      '.strip())                                            # exercise 30

challenge = '30DaysOfPython'                                                        # exercise 31
print(challenge.isidentifier())
challenge = 'thirty_days_of_python'
print(challenge.isidentifier())

print('# '.join(['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']))                # exercise 32

print("I am enjoying this challenge.\nI just wonder what is next")                  # exercise 33

print("Name\t\tAge\tCountry\tCity")                                                 # exercise 34
print("Asabeneh\t250\tFinland\tHelsinki")

radius = 10                                                                         # exercise 35
area = 3.14 * radius ** 2
print(f"The area of a cricle with radius {radius} is {area} meters square.")

print(f"8 + 6 = {8+6}")                                                             # exercise 36
print(f"8 - 6 = {8-6}")
print(f"8 * 6 = {8*6}")
print(f"8 / 6 = {8/6:.2f}")
print(f"8 % 6 = {8%6}")
print(f"8 // 6 = {8//6}")
print(f"8 ** 6 = {8**6}")