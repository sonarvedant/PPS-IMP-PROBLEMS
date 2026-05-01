"""create a newfile "practice.txt" using python add th efollowing data

Hi everyone 
we are leaning file handling 
using java
i like java programing language

"""
#replace java with python and save the file

with open("4-File handling and Dictionaries\practice.txt", "r") as f:
    data = f.read()
    print("databefore editing is :", data)

    data = data.replace("java", "python")
    print("data after editing is :", data)

# if we use w mode then we can overwrite the data in file 
#means changes in main file 

with open("practice.txt", "w") as f:
    f.write(data)
