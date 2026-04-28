#program to calculate area of square using user defined function
def area_of_square(side):
    area = side * side
    return area 
side = float(input("Enter the side length of the square: "))
area = area_of_square(side) 
print("The area of the square is:", area)