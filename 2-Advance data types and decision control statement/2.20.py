"""write a program to show following pattern 
A A A A A
B B B B
C C C
D D
E   

"""
num = 65
for i in range(0,5):
    for j in range(i,5):
        a = a(num+i)
        print(a,"",end="")
    print()