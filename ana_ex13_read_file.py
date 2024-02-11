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
# for loop iterates until there are lines to read in file
for line in open("pelican.txt", 'r'):
    # appends line along with \n
    # lines_list.append(line)
    # leave out the end of line character \n
    # lines_list.append(line[:-1])
    # strip() method to remove the end of line character
    lines_list.append(line.strip())
# print the type of lines_list
print("\n", type(lines_list))
# prints the lines_list
print(lines_list)
# closes the file
file.close()
