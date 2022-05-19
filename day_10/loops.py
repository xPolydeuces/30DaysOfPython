# Day 10: 30 Days of Python Programming

for num in range(11):                                       # exercise 1
    print(num)

num = 0
while num <= 10:
    print(num)
    num += 1

num = 0                                                     # exercise 2
for num in range(10,0,-1):
    print(num)

num = 10
while num >=0:
    print(num)
    num -= 1

for i in range(1,8):                                        # exercise 3
    print('*'*i)

for i in range(8):                                          # exericse 4
    for j in range(8):
        print('#', end=' ')
    print()

for i in range(11):                                         # exercise 5
    print(i, 'x', i, '=', i * i)

for item in ['Python', 'Numpy','Pandas','Django', 'Flask']: # exercise 6
    print(item)

for i in range(101):                                        # exercise 7
    if i % 2 == 0:
        print(i)

for i in range(101):                                        # exercise 8
    if i % 2 != 0:
        print(i)

# LEVEL 2

sum = 0                                                     # exercise 1
for i in range(101):
    sum += i

print("The sum of all numbers is {sum}.")

evens_sum = 0                                               # exercise 2
odds_sum = 0

for i in range(101):
    if i % 2 == 0:
        evens_sum += i
    else:
        odds_sum += 1

print(f"The sum of all evens is {evens_sum}. The sum of all odds is {odds_sum}.")

# LEVEL 3

from countries import countries                             # exercise 1

for country in countries:
    if 'land' in country:
        print(country)

fruit_list = ['banana', 'orange', 'mango', 'lemon']         # exercise 2
fruit_list.reverse()
