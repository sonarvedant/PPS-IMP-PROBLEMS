# program to demonstrate operations on list
L = [1,2,3,4]
print("this is original string", L)

#accesing elements
print("third element ",L[2])
print("last element ",L[-1])

#modifying elements 
L[1] = 12
print("modified list is ", L)

#adding elements 
L.append(5)
print("added element list is ", L )

#removing element (pop is used to remove last item whereas .remove is used to remove by value 
L.remove(1)
print("removed item by using .remove method :", L)
L.pop()
print("removed item by using pop method : ", L)

#sorting list 
# 1. ascending order 
L.sort()
print("sorted list in ascending order is  : " , L )

# 1. descending order 
L.sort(reverse=True)
print("sorted list in descending order is  : " , L )

#reversing a list 
L.reverse()
print("reversed list is :", L )