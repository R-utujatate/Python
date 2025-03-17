'''
Set is the collection of the unordered items.
Each element in the set must be unique & immutable
List and Dictinory can't stored in Sets.
'''

nums={1,2,3,4}
print(nums)
#repeateed elements stored only once, so it resolved to {1,2}
set2={1,2,2,2}
print(set2)
collection = {1,2,3,"hello","world"}
print(collection)
print("Length of =>",len(collection))

#Empty set
Set = set()
print(Set)
print(type(Set))
