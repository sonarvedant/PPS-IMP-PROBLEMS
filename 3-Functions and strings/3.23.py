#program using lambda function to check if a number is even or odd
check_even_odd = lambda num: "Even" if num % 2 == 0 else "Odd"

num = float(input("Enter a number: "))
print("The number is:", check_even_odd(num))