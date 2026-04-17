# program to find wheather given character is vowel or not
char = input("enter a char: ")
if(len(char)==1):
    if char in "aeiouAEIOU":
        print("char is vowel.")
    else:
        print("char is not vowel.")
else:
    print("enter single character only...")