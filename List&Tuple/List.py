'''
List - A built-in data type that stores set of values
It can store elements of different types (integer,float,string,etc)
Strings are immutable in python
Lists are mutable in python
'''

marks=[80.23,27,56.2,80,90.99,78]
print(marks)
print(marks[2])
print(marks[0])

student=["Rutuja","Tate",23,"Rutuja@gmail.com","MS2319"]
print(student)
print(student[3])
print(student[4])

print(len(student))
student[0]="Kishori"

print(student)
print(len(student))