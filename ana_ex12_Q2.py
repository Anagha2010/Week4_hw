# Week 4 homework
# Ques 2.

tup = 'Hello'
# tup is a string of length 5
print(f"Length of: tup = 'Hello' : {len(tup)} (It's a string)\t {type(tup)}")
tup = 'Hello',
# tup is a tuple containing one element
print(f"Length of: tup = 'Hello', : {len(tup)} (It's a tuple when declared with a comma)\t {type(tup)}")

print('\n', '-' * 100, '\nJen - QUESTION 2\n')

# A string is assigned to the variable, tup
tup = 'Hello'

# length function returns how many characters are in the string, then it's printed
print(f'How many characters are in the string: {len(tup)}')

# The tup variable is re-assigned a new value, a tuple with one item
tup = 'Hello',
# How many items are in the tuple is returned by the length function and printed
print(f'How many items are in the tuple: {len(tup)}')
