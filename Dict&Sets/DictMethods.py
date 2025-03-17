student = {
    "name":"rahul kumar",
    "subjects":{
        "phy":97,
        "chem":98,
        "math":95
    }
}
print(student.keys())
#Type-Casting
print(list(student.keys()))
print(tuple(student.keys()))
print("length :",len(list(student.keys())))

print("Values :",student.values())
print("Values list",list(student.values()))
print("Values Tuple :",tuple(student.values()))

#student.items() - returns all elements in the form of tuple
print("items ->",student.items())

#myDict.get("key") - returns the key according to values
print("Access value ->",student.get("subjects"))

#myDict.update(newDict) - inserts the specified items to the dictionary

Country ={
    "Name":"India",
    "Plateu":"Asia",
    "Cities":3000
}
new_dict={"No_States":29,"My_State":"Maharashtra"}
Country.update(new_dict)
print("Dictionary => ",Country)
