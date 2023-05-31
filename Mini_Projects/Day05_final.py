#PASSWORD GENERATOR
'''
Instructions
The program will ask:

How many letters would you like in your password?
How many symbols would you like?
How many numbers would you like?

The objective is to take the inputs from the user to these questions and then generate a random password. Use your knowledge about Python lists and loops to complete the challenge.

Easy Version (Step 1)
Generate the password in sequence. If the user wants
4 letters
2 symbols and
3 numbers
then the password might look like this:fgdx$*924

You can see that all the letters are together. All the symbols are together and all the numbers follow each other as well. Try to solve this problem first.

Hard Version (Step 2)
When you've completed the easy version, you're ready to tackle the hard version. In the advanced version of this project the final password does not follow a pattern. So the example above might look like this:
x$d24g*f9
And every time you generate a password, the positions of the symbols, numbers, and letters are different.'''

from random import randint

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to Password Generator")

#easyversion
def easy_password_generator(letters_needed=4,numbers_needed=4,symbols_needed=2):
    password = ""
    for val in range(letters_needed):
        password+=letters[randint(0,len(letters)-1)]
    for val in range(numbers_needed):
        password+=numbers[randint(0,len(numbers)-1)]
    for val in range(symbols_needed):
        password+=symbols[randint(0,len(symbols)-1)]
    return password

#Hard_Version randomising the o/p password
def hard_password_generator(letters_needed=4,numbers_needed=4,symbols_needed=2):
    password=[]
    for val in range(letters_needed):
        password.append(letters[randint(0,len(letters)-1)])
    for val in range(numbers_needed):
        password.append(numbers[randint(0,len(numbers)-1)])
    for val in range(symbols_needed):
        password.append(symbols[randint(0,len(symbols)-1)])
    #print(len(password))
    new_password=""
    for val in range(len(password)):
        new_password_value=password[randint(0,len(password)-1)]
        new_password+=new_password_value
        password.remove(new_password_value)
    return new_password
        
generator_selection = int(input("Please Enter which Password Generator do you want? \n1 for Easy and 2 for Hard: " ))
if generator_selection==1:
    letters_needed=int(input("How many letters do you want:"))
    numbers_needed=int(input("How many numbers do you want:"))
    symbols_needed=int(input("How many symbols do you want:"))
    print("your easy password could be:"+easy_password_generator(letters_needed,numbers_needed,symbols_needed))
elif generator_selection==2:
    letters_needed=int(input("How many letters do you want:"))
    numbers_needed=int(input("How many numbers do you want:"))
    symbols_needed=int(input("How many symbols do you want:"))
    print("your hard password could be:"+hard_password_generator(letters_needed,numbers_needed,symbols_needed))
