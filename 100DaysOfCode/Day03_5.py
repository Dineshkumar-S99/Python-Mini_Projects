#to create a pizza price calculator 
# Small Pizza: $15
# Medium Pizza: $20
# Large Pizza: $25
# Pepperoni for Small Pizza: +$2
# Pepperoni for Medium or Large Pizza: +$3
# Extra cheese for any size pizza: + $1
bill = 0
pizza_size= input("what size pizza do you want ? \n Type S for small , M for medium and L for large : ")
pepperoni =input("want to add pepperoni ? \n if yes type Y else type N :")
Extra_cheese = input("want some extra cheese? \n if yes type Y else type N :")
if pizza_size == "S" :
    bill += 15
    if pepperoni == "Y":
        bill += 2
        if Extra_cheese =="Y":
            bill += 1
    print(f"your bill amount is :{bill}$")
elif pizza_size == "M":
    bill += 20
    if pepperoni == "Y":
        bill += 3
        if Extra_cheese =="Y":
            bill += 1
    print(f"your bill amount is :{bill}$")
elif pizza_size == "L":
    bill += 25
    if pepperoni == "Y":
        bill += 3
        if Extra_cheese =="Y":
            bill += 1
    print(f"your bill amount is :{bill}$")
else:
    print("you typed a wrong keyword ! check have you entered caps letter")


