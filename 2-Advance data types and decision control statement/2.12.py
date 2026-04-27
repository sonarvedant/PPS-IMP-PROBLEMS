#to calculate sum of n natural numbers and finding out teh average of it using while loop
# n = int(input("enter value of n : "))
n = 5
sum = 0 
avg = 0.0
i = 1
while i <= 10:
    sum = sum + i
    i = i+1
print("sum is ", sum )
avg = sum/n
print("average is ", avg)