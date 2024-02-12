# Week 4 homework
# Ques 1.

# Initializing list named cheese with 3 values
cheese = ['cheddar', 'stilton', 'cornish yarg']

# trying to add a 'oke' like a string to the list
cheese += 'oke'
print(f"\n{'':<0} {cheese}")

# popping out last three erroneous additions
print(f"{'':<0} {cheese}")
for number in range(0, 3):
    cheese.pop()
    print(f"{'':<0} {cheese}")

# trying to add 'oke' like a list item to the list
cheese += ['oke']
print(f"{'':<0} {cheese}")

# removing it and will add it again in another way
cheese.remove('oke')
print(f"{'':<0} {cheese}")

# adding string to list in proper way using append function
cheese.append('oke')
print(f"{'':<0} {cheese}")

# Adding multiple items to list in one statement
cheese.extend(["mozzarella", "blue cheese"])
print(f"{'':<0} {cheese}")

# Adding another item at the start of the list
cheese[:0] = ['parmesan']
print(f"{'':<0} {cheese}")

# Adding item at start using insert and index as 0
cheese.insert(0, 'cottage-cheese')
print(f"{'':<0} {cheese}")

# Adding in between using index as 2
cheese.insert(2, 'paneer')
print(f"{'':<0} {cheese}")

# sorting the list by default (alphabetically)
cheese.sort()
print(f"{'':<1}Sorted cheese: {cheese}")

