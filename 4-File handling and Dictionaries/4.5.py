#write a python program to split the text line written in the file into words
f = open("4-File handling and Dictionaries\practice.txt", "rt")
line = f.readline()
words = line.split()
print(words)