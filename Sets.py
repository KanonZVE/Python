"""the sets are a type of data structure that can save unique elements
We can define them with {} and his elements will be separated by a ,"""

set1 = {1,2,3}
print (set1)

"""The sets are not like the list or tuples because them cannot be accessed 
Through the index"""

#set1[0] is  error TypeError: 'set' object is not subscriptable

set2 = {1,1,1,2,3}
print (set2)

set3 = {1,2.0,"texto"}
print (set3)

#We can add elements to the set Through the funcion add

set1.add(4)
print (set1)

#with the update funtion we cab add more than 1 element
set1.update([4,5,6])
print (set1)

"""because the set doesn't support repeat elements, we get {1, 2, 3, 4, 5, 6}
with len we can get the amount of numbers in to the set"""

print (len(set1))

#to eliminate an element to the set we can use the funtion discard
set1.discard(2)
print (set1)

#we can use the funtion remove

set1.remove(4)

print (set1)

#we can empty the set with the funtion clear

set1.clear()

print (set1)