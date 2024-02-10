# Week 4 homework
# Ques 1.

cheese = ['cheddar', 'stilton', 'cornish yarg']
cheese += 'oke'
print(f"\n{'':<0} {cheese}")
# popping out last three erroneous additions
print(f"{'':<0} {cheese}")
for number in range(0, 3):
    cheese.pop()
    # print(f"{'':<0} {cheese}")
cheese += ['oke']
print(f"{'':<0} {cheese}")
cheese.remove('oke')
print(f"{'':<0} {cheese}")
# adding string to list in proper way using append function
cheese.append('oke')
print(f"{'':<0} {cheese}")
cheese.extend(["mozzarella", "blue cheese"])
print(f"{'':<0} {cheese}")
cheese[:0] = ['parmesan']
print(f"{'':<0} {cheese}")
cheese.insert(0, 'cottage-cheese')
print(f"{'':<0} {cheese}")
cheese.sort()
print(f"{'':<1}Sorted cheese: {cheese}")
