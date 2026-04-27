#program to display power of number without using formatting characters
base = int(input("enter the base : "))
exponent = int(input("enter the exponent : "))
power = 1
for i in range(exponent):
    power = power * base    
print("power of", base , "to the exponent", exponent, "is", power)