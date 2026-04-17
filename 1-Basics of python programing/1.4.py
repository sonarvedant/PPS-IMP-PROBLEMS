#program to perform all operations (add , subb , multiply ,...) using math library
import math
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def multi(x,y):
    return x*y
def div(x,y):
    return x/y

num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))

print("addition is = " , add(num1,num2))
print("subtraction is = " , sub(num1,num2))
print("multiplication is = " , multi(num1,num2))
print("division is = " , div(num1,num2))
