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
    # if condition checks whether set has been filled with 6 numbers and accordingly
    # changes the value of boolean variable full
    if len(lotto_set) == 6:
        full = True
# the lotto set is printed out.
print(f'\nlotto_set = {lotto_set}')

print('\n', '-' * 100, '\nQUESTION 3 - Lottery\n')

# Stored an empty set to random_numbers variable
random_numbers = set()

# length function checks how many items are in the set, random_numbers,
# while loops runs only while the number of the items in the set are NOT equal to 6
while not len(random_numbers) == 6:

    # random is a module, not an object
    # Therefore, randint() is a function even if it's starting with a dot
    # randint function returns a random integer between 1-50
    # add method adds the random number to the set, random_numbers, only unique numbers are saved
    random_numbers.add(random.randint(1, 50))

# tuple method constructs a tuple from the random_numbers set
# As a tuple, the order of items will now remain the same
numbers_tuple = tuple(random_numbers)

# enumerate function returns the index and value of each item in numbers_tuple
# for loop will iterate through each item
for index_tuple, value_tuple in enumerate(numbers_tuple):

    # if the index is equal to 0, the first item's index, execute this code
    if index_tuple == 0:

        # prints a string announcing the lottery numbers and the value of the first item
        # end= adds a space at the end of the string
        print(f'Lottery Numbers: {value_tuple}', end=' ')

    # if the index is NOT equal to 0, execute this code
    else:
        # prints the rest of the values in the tuple with a space after each one
        print(value_tuple, end=' ')

# map function applies a given function, the string function, to each item of numbers_tuple
# string function converted the lottery numbers into strings
# join method concatenates the strings with a space in between each number
# the string is assigned to the file_numbers variable
file_numbers = ' '.join(map(str, numbers_tuple))

# with statement properly manages resources, automatically closing the file after this block of code is executed
# open function opens the file lottery_history.txt in 'append' mode as the variable, file
with open('lottery_history.txt', 'a') as file:

    # write method adds the string from file_numbers variable and a new line onto lottery_history.txt
    file.write(f'{file_numbers}\n')

    # A string is printed to inform the user that the lottery numbers have been saved
    print('\nSaved in lottery_history.txt\n')

# an empty dictionary is assigned to number_frequency variable
number_frequency = {}

# open function opens lottery.txt again in 'read' mode as the variable, file
with open('lottery_history.txt', 'r') as file:

    # for loop iterates over each line in lottery_history.txt and assigns it to the variable, line
    for line in file:

        # strip() removes the leading and trailing whitespaces of each string
        # split() turns each line into a list. By default, it will divide each item by the spaces
        # The list is stored in numbers_history variable
        numbers_history = line.strip().split()

        # for loop iterates over each item in numbers_history list and assigns them to win_number
        for win_number in numbers_history:

            # try statement defines this as a block of code where exceptions can occur
            try:
                # win_number string is converted into an integer and assigned to history_integers variable
                win_num_integer = int(win_number)

                # get() method returns the value of a specific dictionary key, win_num_integer
                # 0 is set as the default value to return if the key does not exist in the dictionary yet
                # 1 is added to either an existing key's value or a new key with a value of 0
                # The dictionary, number_frequency, will either be assigned an updated value or a new key-value pair
                number_frequency[win_num_integer] = number_frequency.get(win_num_integer, 0) + 1

            # except statement catches the ValueError handle exception that may occur
            # ValueError is raised when an argument is received with the correct type, but invalid value
            except ValueError:

                # Prints a string informing the user that the value in win_number is not an integer
                # This error happens when trying to convert a string to an integer, but the string is not a number
                # Since the randint() method is used, it is an unlikely error, unless the input() function is used
                print(f'Error: {win_number} is not an integer.')

# items method returns key-value pairs as tuples, win number and freq number, from the number_frequency dictionary
# items method always returns a sequence of tuples from a dictionary
# key= specifies a function that determines the sorting criteria for the items of an iterable, an optional parameter
# lambda defines a small, one-line function without giving it a name, an anonymous function
# win_freq: represents each key-value pair as a tuple
# win_freq[1] specifies the value to use for sorting, the second value of each pair, frequency number
# reverse= is a parameter of the sorted function. 'True' sorts the list in descending order
# sorted function returns and stores tuples into a sorted list, assigned to sorted_items variable
sorted_items = sorted(number_frequency.items(), key=lambda win_freq: win_freq[1], reverse=True)

# upper method returns the string in uppercase and prints it
print('lottery history'.upper())

# for loop iterates over each tuple in the sorted_items list, assigning each key and value to variables
for key_number, value_frequency in sorted_items:

    # if the value of the tuple is equal or greater than 3, execute the next code
    if value_frequency >= 3:

        # prints a literal f string of each winning number with a frequency of 3 times or more
        print(f'Winning Lottery Number:{key_number}\t Frequency: {value_frequency}')
