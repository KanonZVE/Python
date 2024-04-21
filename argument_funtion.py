"""the argument funtion need asings parameters, they must be declared
into () and separated with a ,"""

def squared_perimeter (side, units):
    perimeter = side * 4
    print(f"The perimeter is {perimeter} {units}")

print(squared_perimeter(45,"meters"))
#or
print(squared_perimeter(side=45,units="meters"))