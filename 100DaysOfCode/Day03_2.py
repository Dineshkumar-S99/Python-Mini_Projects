# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#bmi formula weight / height square 
final_height = float(height)
final_weight = float(weight)
bmi = round((final_weight / (final_height ** 2)) , 1)
bmi_final = str(bmi)


#under 18.5 - underweight , 18.5 - 25 - normal 
#25 - 30 - overweight , 30-35 - obese, above 35 clinically obese 
#print : your BMI is eg:20 , you are perfectly normal or 
#slightly overweight

if bmi <18.5 :
    print("your BMI is " + bmi_final + " kg/m^2 , you're slightly underweight.")
elif 18.5<bmi <=25 :
    print("your BMI is " + bmi_final + " kg/m^2 , you're are perfectly Normal.")
elif 25 < bmi <=30 :
    print("your BMI is " + bmi_final + " kg/m^2 , you're slightly overweight.")
elif 30 < bmi <=35 :
    print("your BMI is " + bmi_final + " kg/m^2 , you're obese start exersising.")
else:
    print("your BMI is " + bmi_final + " kg/m^2 , you're in need of medical consultation imediately.")
