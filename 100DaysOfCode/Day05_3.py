'''You are going to write a program that calculates the sum of all the even numbers from 1 to 100. Thus, the first even number would be 2 and the last one is 100:
i.e. 2 + 4 + 6 + 8 +10 ... + 98 + 100
Important, there should only be 1 print statement in your console output. It should just print the final total and not every step of the calculation'''


def sum_of_even_numbers(fromvalue,tovalue):
    sum=0
    for val in range(fromvalue,tovalue+1):
        if val%2==0:
            sum+=val
    return sum

print(sum_of_even_numbers(1,100))



#or
def sum_of_even_numbers(tovalue):
    sum=0
    for val in range(2,tovalue+1,2):
      sum+=val
    return sum

print(sum_of_even_numbers(int(input("Enter a Number:"))))
