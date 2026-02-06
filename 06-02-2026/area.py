def calc_rectangle(length, width):
    area = length*width
    preimeter = 2*(length + width)
    return area, preimeter
length = float(input("Enter the length:"))
width = float(input("Enter the width:"))
area, perimeter = calc_rectangle(length, width)
print(f"Area: {area}, perimeter: {perimeter}")
    