def validate_x(x):
    if x < 1:
        raise Exception("the x variable is greater than 1")
    else:
        print("x is less than 1")

x = 0.3
validate_x(x)