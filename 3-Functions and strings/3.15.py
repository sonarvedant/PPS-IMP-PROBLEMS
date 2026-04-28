#program to check no is even or odd
def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

number = float(input("Enter a number: "))
check_even_odd(number)
print("The number is:", check_even_odd(number))