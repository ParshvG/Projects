num = int(input("enter a number: "))
sum = 0
temp = num

def cube(num1):
    return (num1 ** 3)

while temp > 0:
    last_digit = temp % 10
    cube_of_number = cube(last_digit)
    sum = sum + cube_of_number
    temp = temp // 10

if (sum == num):
    print("is a armstrome number ", num)
else:
    print("it is not a armstrome number ", num)