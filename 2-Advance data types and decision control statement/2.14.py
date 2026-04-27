#program to display even or odd numbers between 1 to n 
n = int(input("enter value of n : "))
i = 1 
j = 1 
while i <= n :
    if j%2 == 0 :
        print(j, "is even ")
    else:
        print(j, "is odd")
        