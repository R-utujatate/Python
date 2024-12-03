f=open('file.txt','w')
# overwrites the entire file
f.write("It is very easy language.")
f.close()

fi=open('file.txt','a')
# adds to the file
fi.write("And this is how it works...")
fi.close()

with open("demo.txt","a") as F:
    data = F.write("How are you")
    print(data)