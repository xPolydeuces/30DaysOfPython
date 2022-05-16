# Day 7: 30 Days of Python Programming

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# LEVEL 1

print(len(it_companies))                                                        # exercise 1

it_companies.add('Twitter')                                                     # exercise 2

it_companies.update(['Instagram', 'Meta', 'Xiaomi', 'Huawei', 'Samsung'])       # exercise 3

it_companies.remove('Facebook')                                                 # exercise 4

try:                                                                            # exercise 5
    it_companies.discard('Facebook')
except KeyError:
    print("discard method raises KeyError when value is not in the set") # False

try:
    it_companies.remove('Facebook')
except KeyError:
    print("remove method raises KeyError when value is not in the set") # True

# LEVEL 2

C = A.union(B)                                                                  # exercise 1

A.intersection(B)                                                               # exercise 2

A.issubset(B)       # True                                                        exercise 3

A.isdisjoint(B)     # False                                                       exercise 4

A.update(B)                                                                     # exercise 5
B.update(A)

A.symmetric_difference(B)                                                       # exercise 6
B.symmetric_difference(A)

del A, B                                                                        # exercise 7

# LEVEL 3

age = set(age)                                                                  # exercise 1

# string = immutable, contain only characters, ordered                            exercise 2
# list = mutable, can contain anything, ordered
# tuple = immutable, can contain anything, ordered
# set = mutable, can contain anything, unordered, only unique elements

sentence = "I am a teacher and I love to inspire and teach people."             # exercise 3
sentence = sentence.split(' ')
sentence = set(sentence)
print(f"Sentence 'I am a teacher and I love to inspire and teach people.' has {len(sentence)} unique words.")