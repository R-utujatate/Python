# with open("practice.txt","w") as f:
#     f.write("Hii everyone\nwe are learning file I/O\n")
#     f.write("Using Java.\nI like programming in Java.")


#replace all occurrences of java with python
'''
with open("practice.txt","r") as f:
   data=f.read()

new_data=data.replace("Java","Python")
print(new_data)

with open("practice.txt","w") as f:
   f.write(new_data)

'''
#Search if the word learning is exist in the file or not
word="learning"
with open("practice.txt","r") as f:
    data = f.read()
    if(data.find(word) != -1):
        print("Found")
    else:
        print("not found")


