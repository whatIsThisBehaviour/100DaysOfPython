import random
names = input("Enter names of people ready to pay up the bills separated by comma and space : ").split(",")
for person in names:
    person_paying_bil= random.choice(names)
print(f"{person_paying_bil} is going to pay up the bill for today !")