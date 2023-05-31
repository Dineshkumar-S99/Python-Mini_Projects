#calculate the year is a leap year 

#if year div by 4 have no remainder then it is a leap yr 
# but if we get no remainder then it will become a non leap year
# and also if again we devide by 400 and get no remainder then only it's a leap yr
# eg: The year 2000:
# 2000 ÷ 4 = 500 (Leap)
# 2000 ÷ 100 = 20 (Not Leap)
# 2000 ÷ 400 = 5 (Leap!)
# So the year 2000 is a leap year.

# But the year 2100 is not a leap year because:
# 2100 ÷ 4 = 525 (Leap)
# 2100 ÷ 100 = 21 (Not Leap)
# 2100 ÷ 400 = 5.25 (Not Leap) 


year = int(input("Enter the Year:"))

if year % 4 == 0:
    if year % 100 ==0 and year % 400 == 0:
        print("It's a Leap Year")
    elif year % 100 == 0 and year % 400 != 0:
        print("It's a non leap year")
else:
    print("It's a non leap year")
