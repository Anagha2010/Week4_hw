# Week 4 Homework
# Ex 13 read file

# file handle. File 'pelican.txt' is opened in read mode.
file = open("pelican.txt", 'r')
# slurping the file and storing it in a variable (as string)
limerick = file.read()
# printing the type of variable 'limerick' and then the value
print("\n", type(limerick))
print(limerick)
# closing the file
file.close()

# creating an empty list
lines_list = []
# for loop iterates until there are lines to read in file and closes the file in the end
for line in open("pelican.txt", 'r'):
    # appends line along with \n
    # lines_list.append(line)
    # leave out the end of line character \n
    # lines_list.append(line[:-1])
    # strip() method to remove the end of line character
    lines_list.append(line.strip())
# print the type of lines_list
# no need to close the file as it gets closed at the end of for loop
print("\n", type(lines_list))
# prints the lines_list
print(lines_list, "\n")

# Opening another file
file = open('nests.txt', 'r+')
# slurps the limerick1.txt file in one go - stores the entire content in string variable limerick1
limerick1 = file.read()
# print type and value of limerick1
print(type(limerick1), "\n", limerick1)

# re-doing the iterative read using while loop instead of for
# initialize empty list
lines_list2 = []
# since the file cursor is currently at the end of file, we are seeking the start of file.
file.seek(0)
# while loop runs until break command is executed
while True:
    # line variable is assigned the string value returned by readline() after stripping the newline character
    line = file.readline()
    # checks if there is no line left to read in the file
    if not line:
        # breaks the loop and goes to code after loop outside
        break
    # appends line to lines_list2
    lines_list2.append(line)
# printing the type of lines_list2 followed by its value
print("\n", type(lines_list2))
print(lines_list2)
# close the file nests.txt
file.close()

# DOLPHIN TXT - Jen --------------------------------------------------------------------
print('\n', '-' * 100, '\n')

# Created an empty list and assigned it to the dolphin_word_list variable
dolphin_word_list = []

# Created an empty list and assigned it to the dolphin_line_list variable
dolphin_line_list = []

# with statement automatically closes the file after this block of code is executed
# open() function opens the dolphin.txt file in read mode, for reading only, as the dolphin_file variable
with open('dolphin.txt', 'r') as dolphin_file:

    # the next function returns the next item in an iterable object, like iterator
    # An iterator is an object that allows sequential access to elements in a stream of data.
    # A file object returned by the open() function is an iterator
    # next() reads the next line from the file and returns it.
    # In this case, it is the 1st line stored in a variable, first_line
    first_line = next(dolphin_file)

    # A string about the returned data type is printed, including the type of the first_line variable
    print('The returned data type from dolphin.txt is:', type(first_line), '\n')

    # .seek() method changes the current position of the file pointer within a file
    # 0 indicates the beginning of the file, bringing the file pointer to the start of the dolphin.txt file
    dolphin_file.seek(0)

    # for loop iterates over each line in dolphin.txt and stores it in the line variable
    for line in dolphin_file:

        # .strip() method removes whitespace from both ends of a string
        # if a line contains any non-white space characters to apply .strip() on, execute the next code
        # if there are ONLY white spaces on a line, do NOT execute the next code
        if line.strip():

            # strip() removes the white space from the start and end of each line
            # append() method adds a single element to the end of a list
            # append() adds the whole string line as a value in dolphin_line_list
            dolphin_line_list.append(line.strip())

            # split() method converts the line to a list, using space as the default separator for values
            # extend() method adds elements of an iterable, the new list, to the end of a list, dolphin_word_list
            dolphin_word_list.extend(line.split())

# prints the dolphin_word_list and a string about the number of values that list has
print(f'{dolphin_word_list}\n\nThis list has {len(dolphin_word_list)} values.\n')

# prints each line in dolphin.txt without any empty lines
# for loop iterates over each value in dolphin_line_list and stores it in line
for line in dolphin_line_list:

    # each value or line is printed
    print(line)
