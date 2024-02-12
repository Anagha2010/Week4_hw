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
