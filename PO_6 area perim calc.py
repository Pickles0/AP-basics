# ask the user for height and width
# (assume they put in valid data)
width = float(input("Width: "))
height = float(input("height: "))
# Calculate area / perimeter
area = width * height
perimeter = 2 * (width + height)
# output area / perimeter
print()
print(f"perimeter: {perimeter} units")
print(f"area: {area} square units")