#error



#write a program to write/appemnd n number of lines to file and display all these lines as output
n = int(input("enter number of line: "))
f = open("4-File handling and Dictionaries\practice.txt","a")
for i in range(n):
    line = input("enter line: ")
    f.write("\n",line)
f.close

print("new edited file content is :")
x = open("4-File handling and Dictionaries\practice.txt","rt")
print(x.read())
x.close()