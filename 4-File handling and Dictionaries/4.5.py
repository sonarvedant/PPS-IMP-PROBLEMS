#with syntax we can open a file and it will automatically close the file after the block of code is executed
with open("demo.text", "r") as f:
    data = f.read()
    print(data)


# as good programmer we close the file but in with it is not necessary 