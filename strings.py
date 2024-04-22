my_string = "My String"
my_other_string = "My Other String"

#With the len funtion, we can get the longitute of the string

print(len(my_string))
print(len(my_other_string))

#we can concatenate 2 variables with a "+" 
print(my_string + " " + my_other_string)

#if we put \n insite the string variable, we can get a line jump

my_new_line_string = "This is a string\nwith line jump"
print(my_new_line_string)

#to start the sentence with a tabulation, we need put \t in the begining

my_tab_string = "\tThis is a string with tabulation"
print(my_tab_string)

my_scape_string = "\\tThis is a scape  \\n String"
print(my_scape_string)

name = "Joan"
surname = "Sanchez"
age = 33

#format

print("My name is {} {} and i'm {} years old" .format(name, surname, age))
print("My name is %s %s and i'm %d years old" %(name, surname, age))
print(f"My name is {name} {surname} and i'm {age} years old")

#funtions

language = "python"

print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
print("1".isnumeric())
print(language.lower())
print(language.lower().isupper)





