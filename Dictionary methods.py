#[23:01, 13/07/2021] Teju🥰: Dictionary Methods

Dict1 = {1:'one', 2:'two'}

#copy()=Returns a copy of the dictionary
new = Dict1.copy()
print('Dict1: ', Dict1)
print('New: ', new)

#fromkeys()=Returns a dictionary with the specified keys and value
Vowels = {'a', 'e', 'i', 'o', 'u'}
value = 'vowel'
vowels = dict.fromkeys(Vowels, value)
print(vowels)

#get()=Returns the value of the specified key
person = {'name': 'Lokesh', 'age': 20}
print('Name: ', person.get('name'))
print('Age: ', person.get('age'))
print('DOB: ', person.get('DOB',2000))


#items()=Returns a list containing a tuple for each key value pair
sales = { 'apple': 2, 'orange': 3, 'grapes': 4 }
print(sales.items())


#keys()=Returns a list containing the dictionary's keys
person = {'name': 'Lokesh', 'age': 20 }
keys = person.keys()
print(keys)


#pop()=Removes the element with the specified key
person = {'name': 'Lokesh', 'age': 20 }
person.pop("age")
print("person=",person)


#popitem()=Removes the last inserted key-value pair
person = {'name': 'Lokesh', 'age': 20 , 'Gender' : 'male'}
print("person=",person)
person.popitem()
print("person=",person)


#setdefault()=Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
person = {'name': 'Lokesh', 'age': 20}
age = person.setdefault('age')
print('person = ',person)
print('Age = ',age)


#update()=Updates the dictionary with the specified key-value pairs
person = {'name': 'Lokesh', 'age': 20}
d={ 'DOB': 2000 }
person.update(d)
print("person=",person)


#values()=Returns a list of all the values in the dictionary
person = {'name': 'Lokesh', 'age': 20}
print(person.values())


#clear()=Removes all the elements from the dictionary
person = {'name': 'Lokesh', 'age': 20}
person.clear()
print("Pesrson=",person)
