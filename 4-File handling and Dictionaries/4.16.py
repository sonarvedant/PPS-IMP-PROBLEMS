#program to check whather the word is in  file and on which line
f = open("4-File handling and Dictionaries\practice.txt", "r")
word = "learning"
data = True
line = 1
while data:
    data = f.readline()
    if word in data:
        print(f"word is present in line {line}")
    line += 1
