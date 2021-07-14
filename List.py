#List Methods

list=["a","b","c","d","1"]

#append()=Adds an element at the end of the list
list.append("hi")
print("list=",list)


#copy()=Returns a copy of the list
list.copy()
print("list=",list)


#count()=Returns the number of elements with the specified value
count=list.count('1')
print("count=",count)


#extend()=Add the elements of a list (or any iterable), to the end of the current list
list.extend('2')
print("list=",list)


#index()=Returns the index of the first element with the specified value
index=list.index('2')
print("Index=",index)


#insert()=Adds an element at the specified position
list.insert(2,"0")
print("list=",list)


#pop()=Removes the element at the specified position
list.pop(4)
print("list=",list)


#remove()=Removes the item with the specified value
list.remove("2")
print("list=",list)


#reverse()=Reverses the order of the list
list.reverse()
print("list=",list)


#sort()=Sorts the list
list.sort()
print("list=",list)


#clear()=Removes all the elements from the list
list.clear()
print("list=",list
