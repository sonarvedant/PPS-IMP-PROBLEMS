#program to read first 10 characters from file and display it
f = open("4-File handling and Dictionaries\practice.txt","rt")
content = f.read(10)
print(content)
f.close