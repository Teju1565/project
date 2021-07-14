#QUES:Can we update the Value of Key in Dictionary and how?

#Ans:Yes we can update the value of a key in dictionary by using the keyword dict.update([new key value])
#Syntax: dict.update([other])
#Parameters: This method takes either a dictionary or an iterable object of key/value pairs (generally tuples) as parameters.
#Returns: It doesn’t return any value but updates the Dictionary with elements from a dictionary object or an iterable object of key/value pairs.


#EXAMPLE 1:
# Python program to show working of update() method in Dictionary

Dict1 = { 'Name': 'Lokesh', 'Age': '20', }
Dict2 = { 'Age': '21' }

# Dictionary before Updation
print("Original Dictionary:")
print(Dict1)

# update the value of key 'Age'
Dict1.update(Dict2)
print("Dictionary after updation:")
print(Dict1)


#EXAMPLE 2:
# Python program to show working of update() method in Dictionary

# Dictionary with single item
Dict1 = { 'Name': 'Lokesh'}

# Dictionary before Updation
print("Original Dictionary:")
print(Dict1)

# update the Dictionary with iterable
Dict1.update(Age= '20', Gender = 'Male')
print("Dictionary after updation:")
print(Dict1)
