#write a program to display the result such as distinction , first class , second class , passor fail based on marks entered by user 
a = int(input("enter the marks : "))
if a >= 75 :
    print("A grade")
elif a >= 60 :
    print("B grade")
elif a >=45 :
    print("c grade")
else: 
    print("you are fail .")