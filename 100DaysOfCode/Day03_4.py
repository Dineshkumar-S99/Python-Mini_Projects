#to create a roller coster bill machine 
#steps if the person above 120cm he can ride else he cannot
#if age less than 12 bill is 5$ and less than 18 then 7$ else 12$
#if they want a picture add extra 3 dollars to the existing bill

height = int (input ("what is your height in cm: "))
bill = 0
if height >=120 :
    age = int(input("what is your age : "))
    if age <= 12 :
        bill = 5
    elif age <= 18 :
        bill = 7 
    else :
        bill = 12 

    picture = input(" want your picture to be printed? \n type yes or no : ")
    if picture == "yes" :
        bill +=3
    print(f"your bill amount is {bill}$.")
else :
    print("you're not eligible to ride the roller coster")

