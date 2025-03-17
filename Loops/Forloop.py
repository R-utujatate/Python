'''
loops are used for sequential traversal.For traversing list,string,tuples etc
'''
List=[1,2,3]
for el in List:
    print(el)

numbers=(1,2,3,4,5,6,)
print("Print the even numbers")
for el in numbers:
    if(el % 2 == 0):
        print(el)
