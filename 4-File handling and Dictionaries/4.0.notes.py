"""
File handling and Dictionaries
FILE : file is named location on disc to store information 
file have persistent data structure (memory stored permanantly in secondary memory) 
every file is located by its path . and character \ used in pathname is called delimiter.

absolute path : it is the complete path from the root directory to the file.
relative path : it is the path from the current working directory to the file.

Types of file 
1] Text file : data present in form of characters 
the text ascii file is simple file containign collection of characters that are readable to human 
operations performed - opening file , reading file ,writing file , appending data to file 
can be oped using texxt editor like notepad
cannot be corrupted easily
In text file each line contains any nuumber of characters include one or more characters including a special characters that denotes the end of file 
eacch line of text have macimum 255 characters
when data is written to file each newline character is converted into carriage return/line feed character, 
similarly when data is read from file each carriage return feed character is conveted to newline character.


2] Binary file: data present in encoded form 
image , audio , text data can be present 
even if single bit is changed file is corrupted 
cant read using text editor like notepad

OPENING file
in python there is built in function open() to open file 
syntax: file_object = open(file_name,mode)
another syntax to open file(open with): with open("file_name","mode" as f
we can open it in text or binary mode , there are various mode to open file
r - open file for reading
w - open file for writing 
x - open file for creation only
a - open file for aappending mode
t - open file in text mode
b - open files in binary mode
+ open file for updation (reading and writing)

File object attribute  : on opening file object is returned . 
it is possible to get different types of information related to file object usin gattributes with the file object

CLosing file syntax : file_name.close()

Reading the file 
if we diretly write f.read() then it will display output with /n character 
if we write print(f.read()) then it will display output as it is 

readline method():
this method allowss us to read a single line from file . 
when file reaches to the end it returns an empty sring

readlines method():
this method read and used to print all the lines files

list() method:
this method os used to display contents of file as a list
















Dictionaries
operations
1] adding items to dictionaries
2] remove items
3] updation of value in dictionaries
4] checking lenght







"""