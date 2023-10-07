num = int(input("enter a number: "))
def is_prime_number(num, i = 2):
    while i < num:
        if (num % i == 0):
            return False
        i = i + 1
    return True

print ("is prime number", is_prime_number(num))