#program to find a specific word in the file
word = "learning"
with open("4-File handling and Dictionaries\practice.txt", "r") as f:
    data = f.read()
    if word in data:
        print("word is present in file")
    else:
        print("word is not present in file")