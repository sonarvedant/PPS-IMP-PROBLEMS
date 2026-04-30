f = open("demo.text", "r")
data = f.read()
print(data)
print(type(data))
f.close()

#if we write read(5) it will read first 5 characters from file and return it as string
#