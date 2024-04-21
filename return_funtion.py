"""def square_perimeter(side):
    perimeter = side * 4
    return perimeter

def square_area(side):
    area = side * side
    return area"""

def square_calculate(side):
    perimeter = side * 4
    area = side * side
    return perimeter, area

area, perimeter = square_calculate(side=5)
resultado = square_calculate(side=5)

"""perimeter = square_perimeter(side=5)
area = square_area(side=5)"""

print(f"Area: {area}, Perimeter: {perimeter }")
print(resultado)