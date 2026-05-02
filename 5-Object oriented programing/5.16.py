class student:
    def __init__(self,fullname,marks):
        self.name = fullname 
        self.marks = marks
        # here usings sel.name bcoz it is diff or every student 
        # we can directly create variable if data commmon for all
        print("adding info via parameter and argument")

s1 = student("karan",92)
print(s1.name, s1.marks)

s2 = student("arjun", 69)
print(s2.name,s2.marks)