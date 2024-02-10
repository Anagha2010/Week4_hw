# Week 4 homework
# Ques 3 - lotto

import random

lotto_set = set()
full = False
while not full:
    lotto_set.add(random.randint(1, 50))
    if len(lotto_set) == 6:
        full = True
print(f'lotto_set = {lotto_set}')
