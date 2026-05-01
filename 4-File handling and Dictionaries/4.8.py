#program to write multiple lines to a text file using writelines() method.
#this program after running will overwrite the practice.txt file (means all data is replaced)
#to prevent this we can use append method (just use 'a' or 'ab' mode)
f = open("4-File handling and Dictionaries\practice.txt","a")
lines= ["practice make man perfect\n programing is easy"]
f.writelines(lines)
f.close