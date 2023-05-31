#learning to generate random integer and float

#to generate random we want to import the random module that's what we do first
import random

#to generate random integer (here it will include both the starting and ending nu8mbers)
print(random.randint(1 ,10))

#to generate random float (this will exclude the starting and ending numbers)
print(random.random())

#above will generate only values between 0 to 1)
#to get the values higher we will multiply with what values we want

print(random.random()*5)
# this will print values between 0 to 5

