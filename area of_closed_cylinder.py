import math
radius = float(input("Please enter the Radius of the cylinder: "))
height =float(input("Please enter the Height of the cylider: "))
def area_of_cylider():
    pi = 3.142
    area = float(pi*radius*radius*height)
    answer = (round(area,2))
    print(f"The Are of the cylinder is {answer}")
area_of_cylider()    
    