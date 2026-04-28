#program to swap two numbers using user defined function
def swap_numbers(a, b):
    print("Before swapping:")
    print("First number:", a)
    print("Second number:", b)
    temp = a 
    a = b
    b = temp
    print("After swapping:")
    print("First number:", a)   
    print("Second number:", b)

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
swap_numbers(num1, num2)    
