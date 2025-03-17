'''
set.add(el) - adds an element
set.remove(el) - removes the element
set.clear() - empties the set
set.pop() - removes a random value
set is mutable but elements are immutable
'''

collection =set()

collection.add(2)
print(collection)
collection.add("Hello")
print(collection)
collection.add(3)
print("Set is => ",collection)
print("\n")
collection.remove("Hello")
print("Updated Set => ",collection)

collection.clear()
print("cleared set :",collection)

new = {4,2,5,6,1}
print(new)
new.add(("Hello","Rutuja"))
print(new)

print("Poped value",new.pop())
print(new)