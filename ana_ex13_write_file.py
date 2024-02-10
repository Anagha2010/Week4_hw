file = open("pelican.txt", "w+")
file.write("A wonderful bird is the pelican,\n")
file.write("His bill holds more than his belican.\n")
lines = ["He can take in his beak,\n", "Enough for a week,\n",
         "But I am damned if I see how the helican."]
file.writelines(lines)
