from figures.square import square_area, square_perimeter
from figures.circle import circle_area, circle_perimeter
#variables
side = 4
radius = 5

square = {
    "side" : side,
    "area" : square_area(side),
    "perimeter" : square_perimeter(side)
}

print("square: ", square)

circle = {
    "radius" : radius,
    "area" : circle_area(radius),
    "perimeter" : circle_perimeter(radius)
}


print("circle: ", circle) 