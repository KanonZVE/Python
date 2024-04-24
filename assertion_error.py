def calculate_average(list):
    assert len(list)>0, "The list is empty"
    return sum(list) / len(list)

average = calculate_average(list=[1,3,5])
print(average)