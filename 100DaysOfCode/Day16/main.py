from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


#machine = "on"
#while machine=="on":
#    pass
menu=Menu()
#print(menu.get_items())

user_input=input(f"what would you like? {menu.get_items()} \n")
if user_input=="report":
    CoffeeMaker().report()
else:
    item=menu.find_drink(user_input)
    if CoffeeMaker().is_resource_sufficient(item):
        CoffeeMaker().make_coffee(item)
