'''
Dictinaries are used to store data values in key:value pairs
They are unordered,mutable(changeable) & don't allow duplicate keys
'''
Student = {
    "Name":"Rutuja",
    "DOB":"15th-March-2001",
    "Height":167,
    "Weight":"60kg",
    "Is_adult":True
}
print(Student)
print(Student["DOB"])
Student["Name"]="Kishori"
print(Student)
Student["Sirname"]="Tate"
print(Student)
Student["Sirname"]="Sonwane"#Overwrite



Cars ={
    "BMW":["Black",60,"Sunroof"],
    "Oddy":("Navy blue",40,"Without Sunroof")
}
print(type(Cars))
print(Cars["Oddy"])

null_dict ={}
null_dict["Fruit"]="Apple"
print(null_dict)
