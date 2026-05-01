#program to display values of file object attributes
f = open("4-File handling and Dictionaries\practice.txt", "r+")
print("file name is ",f.name)
if (f.close == True):
    print("file is closed")
else:
    print("file is open")
print("file mode is :",f.mode)