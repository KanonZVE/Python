def calculate_average(list):
    assert len(list)>0, "The list is empty"
    return sum(list) / len(list)

try: 
    average = calculate_average(list=["texto"])
    print(average)
except AssertionError as assert_error:
    print(assert_error)
except Exception as e:
    print ("The funtion don't calculate the average")
    print(e)