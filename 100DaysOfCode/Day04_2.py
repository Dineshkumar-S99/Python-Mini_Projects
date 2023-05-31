#to generate random head and tails
import random

#randint will generate a random number between the two numbers
coin= random.randint(1,2)
if coin == 1:
    print("Head")
else:
    print("Tail")
