# Week 4 homework
# Ques 3 - lotto

# Importing math module to use the randint function
import random

# We are asked to create a collection type to store 6 unique numbers ranging from 1 to 50
# Using a set constructor to create an empty set object to store the numbers (because set values are unique)
lotto_set = set()
# boolean variable full is declared and assigned value False
full = False
# while loop runs as long as condition 'not full' is true
while not full:
    # add method is used to add elements to set, each time a random integer
    lotto_set.add(random.randint(1, 50))
    # if loop checks the condition if set has been filled with 6 numbers and accordingly
    # changes the value of boolean variable full
    if len(lotto_set) == 6:
        full = True
# the lotto set is printed out.
print(f'\nlotto_set = {lotto_set}')
