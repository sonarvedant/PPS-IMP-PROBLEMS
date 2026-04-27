# program to find given number is prime or not
n = int(input("enter value of n : "))
for i in range(2, n):
    if(n%i) == 0:
        