#Paint Area Calculator
'''
Instructions
You are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall. 
Given a random height and width of wall, calculate how many cans of paint you'll need to buy.

number of cans = (wall height x wall width) ÷ coverage per can.

e.g. Height = 2, Width = 4, Coverage = 5
number of cans = (2 * 4) / 5
               = 1.6

But because you can't buy 0.6 of a can of paint, the result should be rounded up to 2 cans.'''

print("Welcome to Paint Calculator")

paint_coverage=5
def paint_calculator(height_of_wall, width_of_wall):
    no_of_cans_needed=(height_of_wall*width_of_wall)/paint_coverage
    return round(no_of_cans_needed)
height_of_wall = int(input("enter the wall height: "))
width_of_wall = int(input("enter the wall width: "))
print(f"Number of paint cans needed are:{paint_calculator(height_of_wall,width_of_wall)}")


#here problem arise when value less than 0.5 it decreases eg:5.2 converted to 5 not 6 
#we use different method called ceil from math module

import math
def paint_calculator(height_of_wall, width_of_wall):
    no_of_cans_needed=(height_of_wall*width_of_wall)/paint_coverage
    return math.ceil(no_of_cans_needed)
height_of_wall = int(input("enter the wall height: "))
width_of_wall = int(input("enter the wall width: "))
print(f"Number of paint cans needed are:{paint_calculator(height_of_wall,width_of_wall)}")