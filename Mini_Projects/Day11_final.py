#BLACK JACK
from random import randint

#if A -> default value is 11 and if above 21 it can be set as 1, and K,Q,J values are equal to 10
Ace=11
King,Queen,Jack=10,10,10

#print(K,Q,J)
cards=[Ace,2,3,4,5,6,7,8,9,10,King,Queen,Jack]
users_value=[]
computers_value=[]

def first_choices(cards,users_value,computers_value):
    value=2
    while value>0:
        users_value.append(cards[randint(0,len(cards)-1)])
        computers_value.append(cards[randint(0,len(cards)-1)])
        value-=1
    return users_value,computers_value

def adding_vals(values):
    total=0
    for val in values:
        total+=val
    return total     

users_total=0
computers_total=0
def blackjack_first(cards,users_value,computers_value,users_total,computers_total):
    first_choices(cards,users_value,computers_value)
    users_total=adding_vals(users_value)
    computers_total=adding_vals(computers_value)
    print(users_total, "com",computers_total)

blackjack_first(cards,users_value,computers_value,users_total,computers_total)




#while True:
    #pass
#print(cards[0],cards[-2])