# Day 6: 30 Days of Python Programming

# LEVEL 1

empty_tuple = ()                                                # exercise 1

brothers = ('Emilio', 'Ryoru', 'Astolfo')                       # exercise 2
sisters = ('Yuko', 'Nanachi', 'Emilia')

siblings = brothers + sisters                                   # exercise 3

print(f"I have {len(siblings)} siblings.")                      # exercise 4

family_members = siblings + ('Dad', 'Mom')                      # exercise 5

# LEVEL 2

(brother1, brother2, brother3, sister1, sister2, sister3, dad, mom) = family_members        # exercise 1

fruits = ('banana', 'orange', 'mango', 'lemon')                                             # exercise 2
vegetables = ('tomato', 'potato', 'cabbage','onion', 'carrot')
animal_products = ('milk', 'cheese', 'honey', 'meat')
food_stuff_tp = fruits + vegetables + animal_products

food_stuff_lt = list(food_stuff_tp)                                                         # exercise 3

print(food_stuff_lt[:len(food_stuff_lt)//2]+food_stuff_lt[len(food_stuff_lt)//2+1:])        # exercise 4

print(food_stuff_lt[3:])                                                                    # exercise 5
print(food_stuff_lt[:-3])

del food_stuff_tp                                                                           # exercise 6

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')                     # exercise 7
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)