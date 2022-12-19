import random

given_name = []
chosen_name = []
family_name = []

with open('given_name.txt', "r", encoding='utf-8') as f:
    given_name = list(f)
with open("chosen_name.txt", "r", encoding='utf-8') as f:
    chosen_name = list(f)
with open("family_name.txt", "r", encoding='utf-8') as f:
    family_name = list(f)

names = []
for i in range(1):
    names.append(random.choice(given_name))
    names.append(random.choice(chosen_name))
    names.append(random.choice(family_name))

print (''.join(names))