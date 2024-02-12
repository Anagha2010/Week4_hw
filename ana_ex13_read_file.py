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
