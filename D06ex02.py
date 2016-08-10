import random

with open("random_numbers.txt", "w") as f:
    for i in range(1,11):
        f.write(str(random.randint(1,100))+'\n')
