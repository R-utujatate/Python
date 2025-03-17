'''
Range function returns a sequence of numbers,
starting from 0 by default,
and increments by 1(by default),
and stops before a specified number

range(start?,stop,step?)
'''
print("Print elements in range 1 to 5 :")
for el in range(1,5):
    print(el)

print("print elements til 10 : ")
for num in range(10):
    print(num)


print("print element in range 1 to 15 with step size 3 :")
for digit in range(1,15,3):
    print(digit)

print("Multiplication table :")
n=int(input("enter the number : "))
for i in range(1,11):
    print(n*i)