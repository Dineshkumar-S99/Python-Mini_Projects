#Prime number checker

"prime numbers are nothing but the numbers that are divisible by only 1 and itself"

print("Prime number checker")
def prime_number_checker(given_num):
    for i in range(2,given_num+1):
        if given_num%i==0 and i<given_num:
            return f"{given_num} is not a prime number"
            break
        elif given_num%i==0 and i==given_num:
            return f"{given_num} is a prime number"
print(prime_number_checker(int(input("Enter the number:"))))

#another method
def prime_number_checker(given_num):
    is_prime=True
    for i in range(2,given_num):
        if given_num%i==0:
            is_prime=False
    if is_prime:
        return f"{given_num} is a prime number"
    else:
        return f"{given_num} is not a prime number"
print(prime_number_checker(int(input("Enter the number:"))))