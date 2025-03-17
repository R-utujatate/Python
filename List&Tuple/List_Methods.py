'''
list.append() - adds one element at the end
list.sort() - sorts in ascending order
list.sort(reverse=True) - sorts in descending order
list.reverse() - reverse list
lists.insert(idx,ele) - insert element at index
list.remove() - remove first occurrence of element
list.pop(idx) - removes element at index

'''

fruits = ['Banana','Apple','Grapes','Orange']
fruits.append('Pineapple')
print("Appended list ->",fruits)
fruits.sort()
print("Sorted list ->",fruits)
fruits.sort(reverse=True)
print("Descending ordered sorted list ->",fruits)
fruits.reverse()
print("Reversed list ->",fruits)
fruits.insert(1,'Jackfruit')
print("Element injecting at perticular index ->",fruits)

list = [2,3,1,4,3]
list.remove(3)
print(list)
list.pop(2)
print(list)

