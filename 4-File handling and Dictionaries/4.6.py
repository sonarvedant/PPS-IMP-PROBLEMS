# write a program that counts number of lines and tabs character in file
f = open("4-File handling and Dictionaries\practice.txt","rt")
file = f.read()
tabs = 0
lines = 0
for char in file:
    if char == '\t':
        tabs+=1
    if char == '\n':
        lines+=1
print("tabs are :",tabs)
print("lines are : ",lines+1)
