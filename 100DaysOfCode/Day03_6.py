#LOVE CALCULATOR here it takes the letters t r u e and add them in 10's place 
#and take L O V E from the provided name and add them to the 1's place 
#and provide the last percentage of true love between those 


print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()

letter_T = name1.count("t") + name2.count("t")
letter_R = name1.count("r") + name2.count("r")
letter_U = name1.count("u") + name2.count("u")
letter_E = name1.count("e") + name2.count("e")

letter_L = name1.count("l") + name2.count("l")
letter_O = name1.count("o") + name2.count("o")
letter_V = name1.count("v") + name2.count("v")
letter_E = name1.count("e") + name2.count("e")

print(f"the number of t in both names : {letter_T}")
print(f"the number of t in both names : {letter_R}")
print(f"the number of t in both names : {letter_U}")
print(f"the number of t in both names : {letter_E}")
print(f"the number of t in both names : {letter_L}")
print(f"the number of t in both names : {letter_O}")
print(f"the number of t in both names : {letter_V}")
print(f"the number of t in both names : {letter_E}")

true_per= str(letter_T + letter_R + letter_U + letter_E)
love_per= str(letter_L + letter_O + letter_V + letter_E)

print ("your True Love Percentage is : " + true_per + love_per)
