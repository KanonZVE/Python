"""The objects by themselves dont have properties, the properties must be
defined in a method created for the classes, called init
This method allow us to define the initials values of the object
The funtion init is the builder of the classes, and they ever execute when 
the object is created"""

class people:
    pass

pedro = people()
print(type(pedro))

paco = people()
print(type(paco))

#pedro and paco are diferents objects with the same class
print(pedro == paco)

class people:
    attribute = 123
    """he self variable represent the instance of the clase and 
    through of her we can access ti the properties and funtions 
    of the class"""
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def turn_years(self):
        self.age += 1
        print(f"Happy Birthay #{self.age} {self.name}")

paco = people(name="Paco", age=32)

paco.turn_years()

print(paco.name)
print(paco.age)
print(paco.attribute)

class worker(people):
    def __init__(self, total_hours, name, age):
        super(worker, self).__init__(name, age)
        self.total_hours = total_hours

    def work(self, work_hours):
        self.total_hours += work_hours
        print(f"You are a worked {work_hours} hours")
        print(f"Total hours: {self.total_hours}")

paco = worker(name = "Paco", age = 33, total_hours = 30)
paco.work(work_hours = 8)
paco.turn_years()
