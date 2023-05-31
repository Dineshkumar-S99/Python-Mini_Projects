# Eample Input
# Angela, Ben, Jenny, Michael, Chloe
# Note: notice that there is a space between the comma and the next name.

# Example Output
# Michael is going to buy the meal today!
# Hint
# You might need the help of the len() function.

# Split string method
import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
#to get the lenth of the list so that we can use random module to generate a random number 

names_choice_number= len(names)
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#here the list index starts from 0 where len fun starts from 1 so we will subtract one from the len
names_pick=random.randint(0,len(names)-1)
weighter_selected_name=names[names_pick]
print(f"the person who wants to pay is : {weighter_selected_name}")


# or we can simply write the code as 
names_weighter_pick = random.choice(names)
print(f"the person who wants to pay is : {names_weighter_pick}")
