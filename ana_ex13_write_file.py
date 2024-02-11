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
# pelican.txt got created on running the above code.
# \n is useful and the file pelican.txt holds a set of lines one below the other
