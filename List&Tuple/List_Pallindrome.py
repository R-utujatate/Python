#Program to check if a list contains a palindrome of elements.(Hint:use copy() method)

List = [1,2,1,1]
List2=List.copy()
print(List2)
List2.reverse()
print(List2)
if(List == List2):
    print("List is pallindrome")
else:
    print("Not a pallindrome")