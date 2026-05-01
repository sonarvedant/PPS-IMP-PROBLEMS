#program to write multiple lines to a text file using writelines() method.
f = open("4-File handling and Dictionaries\practice.txt","wt")
lines= ["practice make man perfect\n programing is easy"]
f.writelines(lines)
f.close