# the program output should be 

# Welcome to the tip calculator.
# what was the total bill? eg $124.56
# what percentage tip would you like to give ? 10. 12 . or 15?  eg:12
# How many people to split the bill? eg:7
# Each person should pay: eg $19.93

print('"Welcome to the tip calculator"')
bill=input("what was the total bill? $")
tip_percentage= input("what percentage tip would you like to give ? 10. 12 . or 15?")
total_people=input("How many people to split the bill?")
total_bill=float(bill) +((float(bill)/100)* float(tip_percentage))
splitted_bill= total_bill / float(total_people)
round_splitted_bill= round(splitted_bill ,2)
print(f"Each person should pay: ${round_splitted_bill}")
