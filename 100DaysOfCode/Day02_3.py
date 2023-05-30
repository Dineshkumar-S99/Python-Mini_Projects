# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#bmi formula weight / height square 
final_height = float(height)
final_weight = float(weight)
bmi = int (final_weight / (final_height ** 2))
bmi_final = str(bmi)
print(bmi_final + " kg/m^2")
