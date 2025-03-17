'''
Accessing parts of a string
str[starting_idx:ending_idx] ending idx is not included
Negative index -> Backword counting == staring from -1
'''
str="Whatevere"
print(str[1:4])

str2="Opposite"
slice=str[1:5]
print(slice)
#till last index
print(str2[1:len(str2)])
# OR
print(str2[3:])
# or from starting index [0:4]
print(str2[:3])

##Negative index
print(str[-3:-1])
