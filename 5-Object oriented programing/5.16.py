class student:
    # we can directly create variable if data commmon for all(eg - college name) above def__init__
    college = "COEP"
    def __init__(self,fullname,marks):
        self.name = fullname 
        self.marks = marks
        # here usings sel.name bcoz it is diff or every student 
        print("adding info via parameter and argument")

s1 = student("karan",92)
print(s1.name, s1.marks,s1.college)

s2 = student("arjun", 69)
print(s2.name,s2.marks,s2.college)