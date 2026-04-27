#program to find sum of 1 to n number using for loop
n = int(input("enter value of n : ")) 
sum = 0
for i in range(1, n+1):
    sum = sum + i
print("the sum of ",n,"numbers is ", sum )