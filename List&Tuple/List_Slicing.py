'''
Similar to string slicing
list_name[starting_idx:ending_idx]
ending index is not included
'''

marks=[87,64,33,95,76]
print(marks[1:4])
print(marks[:4]) #including starting index
print(marks[1:]) #incluedes ending index also
print(marks[2:len(marks)])#same as above
print(marks[-3:-1])

