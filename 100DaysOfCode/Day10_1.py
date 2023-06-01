#Write a program to return a number of days in a given year and month

#eg: given i/p: year=2013 month=2, o/p: 28
#eg: given i/p: year=2020 month=2, o/p: 29

def is_leap(year):
    if year%4==0:
        if year%100==0:
            if year%400==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_a_month(year,month):
    days_list=[31,28,31,30,31,30,31,31,30,31,30,31]
    if month<1 or month>12:
        return "you have entered a wrong number, enter between 1 to 12"
    if is_leap(year)==True and month==2:
        return f"Number of Days in given month is {(days_list[month-1])+1}"
    else:
        return f"Number of Days in given month is {days_list[month-1]}"

year=int(input("Enter the year: "))
month=int(input("Enter the month: "))

print(days_in_a_month(year,month))