from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu=Menu()
#print(menu.get_items())

user_input=input(f"what would you like? {menu.get_items()} \n")
item=menu.find_drink(user_input)