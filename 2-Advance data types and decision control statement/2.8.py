#program to print multiplication table of number taken from user
a = int(input("enter num: "))
print("table of", a , "is :")
for i in range(1,11):
    print(a ,"X", i, "=", a*i)