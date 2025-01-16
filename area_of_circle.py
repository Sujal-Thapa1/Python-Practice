# # Function to calculate area of the circle
def area(radius):
    import math
    formula=math.pi *radius**2
    return formula

radii=int(input("Enter the radius of the circle\n"))
output=area(radii)
print(f"{output:.2f}")