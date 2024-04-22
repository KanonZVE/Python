from square import square_area, square_perimeter

side = 5

square = {
    "side" : side,
    "area" : square_area(side),
    "perimeter" : square_perimeter(side)
}

print(square)