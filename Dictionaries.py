"""store the data in pairs, lets call them keys and values, each value is an element
that corresponds a key.
In other programing languages they are known as a JSON and Hashmaps
We definen in to {} and separate the key an the value with : the elements
must be separate with ,"""

language = {
    "name" : "Python",
    "creator" : "Guido"
}
"""In the dictionaries we cant use the index to access the elements """
print (language ["name"])
language ["launch_year"] = 1991
print (language)

"""The keys are uniques, we can't add more than one value of any of them Ej:"""
language ["launch_year"] = 1994
print (language)
"""{'name': 'Python', 'creator': 'Guido', 'launch_year': 1994}

The keys can be whatever type of you want, but most of the time they are
text type"""
language ["features"] = ["simple", "easy", "awesome"]
print (language)
#with values we can get only the list of elements, without the keys.
print (language.values())