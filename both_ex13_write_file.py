# Week 4 homework
# Ex 13 write file

# File is created or opened in updating mode w+ if it already exists
file = open("pelican.txt", "w+")
# writes one line into the file.
file.write("A wonderful bird is the pelican,\n")
# writes another line into the file
file.write("His bill holds more than his belican.\n")
# creates a list of lines
lines = ["He can take in his beak,\n", "Enough for a week,\n",
         "But I am damned if I see how the helican."]
# writing list of lines into the file
file.writelines(lines)
# close the pelican.txt file
file.close()
# pelican.txt got created on running the above code.
# \n is useful and the file pelican.txt holds a set of lines one below the other


# Assign string value to limerick1_str
limerick1_str = ('There was an Old Man with a beard,\nWho said, "It is just as I feared! -\nTwo Owls and a Hen, '
                 '\nFour larks and a Wren, \nHave all built their nests in my beard!"')
# File is created or opened in updating mode w+ if it already exists
file = open("nests.txt", 'w+')
# writing string limerick1_str  into the file
file.writelines(limerick1_str)
# close the nests.txt file
file.close()

# DOLPHIN TXT - Jen -------------------------------------------------------------------------

# Created a list of values as strings, ending with a new line \n and assigned to the lines variable
lines_two = ['In the sea so blue,\n', 'with a flip and a "woo-hoo,"\n', 'dolphins play and jest,\n',
             'showing who\'s the best.\n\n']

# with statement automatically closes the file after this block of code is executed
# open function opens the file dolphin.txt in 'append and read' a+ mode as the variable, dolphin_file
# 'append and read' mode opens the file for both reading and writing. If the file does not exist, it creates a new file.
with open('dolphin.txt', 'a+') as dolphin_file:
    # .write() method writes only a single string onto dolphin.txt
    # .write() method does not include separators or formatting. So \n new lines were included in this string.
    dolphin_file.write('Dolphins have names for each other.'
                       '\n\nThey use a "signature" whistle to identify themselves '
                       'to other dolphins in their group.\n\n')

    # for loop iterates over each value/string in the list, lines variable, and assigns it to dolphin_rhyme variable
    for dolphin_rhyme in lines_two:
        # .writelines() method writes multiple strings from any iterable object, like the list, to a file
        # .writelines() method also does not include formatting or line separators
        # The \n in the lines list values indicates the end of a line for the .writelines() method
        dolphin_file.writelines(dolphin_rhyme)
