class student:
    def __init__(self,fullname):
        self.name = fullname 
        
        print("adding info via parameter and argument")

s1 = student("karan")
print(s1.name)