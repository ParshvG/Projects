def factorial(n):
    if n == 1:
        return 1
    else:
        return (n * factorial(n-1))
    
n = int(input("enter a number here: "))
if n <= 0:
    print("factorial of number less than 1 not possible")
else:
    print("Factorial of the given number is", factorial(n))