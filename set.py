#Sets Method

set1={"1","2","3"}

#add()=Adds an element to the set
set1.add("4")
print("set1=",set1)


#copy()=Returns a copy of the set
set1.copy()
print("set1=",set1)


#difference()=Returns a set containing the difference between two or more sets
set2={"1","2","4"}
set=set1.difference(set2)
print("set=",set)


#difference_update()=Removes the items in this set that are also included in another, specified set
set=set1.difference_update(set2)
print("set=",set1)


#discard()=Remove the specified item
set1={"1","2","3"}
set1.discard("1")
print("set1=",set1)


#intersection()=Returns a set, that is the intersection of two other sets
set1={"1","2","3"}
set2={"1","2","4"}
set3={"2","4","6"}
set=set1.intersection(set2,set3)
print("set=",set)


#intersection_update()=Removes the items in this set that are not present in other, specified set(s)
set1={"1","2","3"}
set3={"2","4","6"}
set=set3.intersection_update(set1)
print("set=",set)
print("set1=",set1)
print("set3=",set3)


#isdisjoint()=Returns whether two sets have a intersection or not
set1 = {1, 2, 3, 4}
set2 = {5, 6, 7}
print('Are set1 and set2 disjoint?=', set1.isdisjoint(set2))

#issubset()	Returns whether another set contains this set or not
print('Are set1 and set2 subsets?=', set1.issubset(set2))

#issuperset()=Returns whether this set contains another set or not
set1 = {'1','2', '3', '4', '5'}
set2 = {'1', '2', '3'}
print(set1.issuperset(set2))


#pop()=Removes an element from the set
set1 = {'1','2', '3', '4', '5'}
set1.pop()
print('set1=',set1)


#remove()=Removes the specified element
set1 = {'1','2', '3', '4', '5'}
set1.remove('2')
print("set1=",set1)


#symmetric_difference()=Returns a set with the symmetric differences of two sets
set1 = {'a', 'b', 'c', 'd'}
set2 = {'c', 'd', 'e' }
print(set1.symmetric_difference(set2))


#symmetric_difference_update()=inserts the symmetric differences from this set and another
set1 = {'a', 'c', 'd'}
set2 = {'c', 'd', 'e' }
result = set1.symmetric_difference_update(set2)
print('set1 =', set1)
print('set2 =', set2)
print('result =', result)


#union()=Return a set containing the union of sets
set1 = {'a', 'c', 'd'}
set2 = {'c', 'd', 2 }
print('set1 U set2 =', set1.union(set2))


#update()=Update the set with the union of this set and others
set1 = {'a', 'b'}
set2 = {'1', '2', '3'}
result = set1.update(set2)
print('set1 =', set1)
print('result =', result)


#clear()=Removes all the elements from the set
set1.clear()
print("set1=",set1
