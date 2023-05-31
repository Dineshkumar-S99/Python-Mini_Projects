'''You are going to write a program that automatically prints the solution to the FizzBuzz game.
Your program should print each number from 1 to 100 in turn.
When the number is divisible by 3 then instead of printing the number it should print "Fizz".
When the number is divisible by 5, then instead of printing the number it should print "Buzz".`
And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"
e.g. it might start off like this:

1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz'''

def to_print_FizzBuzz(tovalue):
    for val in range(1,tovalue+1):
        if val%3==0 and val%5==0:
            print("FizzBuzz")
        elif val%3==0:
            print("Fizz")
        elif val%5==0:
            print("Buzz")
        else:
            print(val)

to_print_FizzBuzz(int(input("Enter a Number:")))
