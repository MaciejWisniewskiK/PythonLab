import random
numpoints = 1000000
incircle = 0
for i in range(numpoints):
    x = random.random()
    y = random.random()
    if x**2 + y**2 <= 1:
        incircle += 1
print(incircle/numpoints*4)