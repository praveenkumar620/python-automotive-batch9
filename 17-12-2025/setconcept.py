mySet={"apple", "banana","pomegranate","apple",False,2,2}
mylist=['a','b']
mySet2={"a","n"}
print(mylist)
empty_set=set()
empty_dict={ }
print(type(mySet))
mylist.add(10)
mylist.discard(10)
mySet.update(mylist)
count=len(mySet)
print(mySet|mySet2)  #Union
print(mySet&mySet2)  #intersection
for fruit in mySet:
  print(fruit)
#true=1
#false=0