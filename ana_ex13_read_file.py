file = open("pelican.txt", 'r')
limerick = file.read()
print("\n", type(limerick))
print(limerick)
file.close()

lines_list = []
for line in open("pelican.txt", 'r'):
    # appends line along with \n
    # lines_list.append(line)
    # leave out the end of line character \n
    # lines_list.append(line[:-1])
    # strip() method to remove the end of line character
    lines_list.append(line.strip())
print("\n", type(lines_list))
print(lines_list)
file.close()
