min = int(input("enter the minimum number: "))
max = int(input("enter the maximum number: "))
def is_palidrome(number):
    temp = number
    reverse = 0
    while number > 0:
        last_digit = (number % 10)
        reverse = (reverse % 10) + last_digit
        number = int(number / 10)
    if (temp == reverse):
        print("it's palidrome")
    else:
        print("it's not a palidrome")


while min <= max:
    print(min)
    is_palidrome(min)
    min = min + 1