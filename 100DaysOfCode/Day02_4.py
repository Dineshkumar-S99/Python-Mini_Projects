# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# eg output : You have 12410 days, 1768 weeks, and 408 months left.

years_left = 90 - int(age) 
days_left = years_left * 365
weeks_left = years_left * 52
months_left = years_left * 12
print(f"you have {days_left} days, {weeks_left} weeks, and {months_left} months left")
