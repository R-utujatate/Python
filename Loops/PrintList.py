names=['radha','krishna','gopal','abhinav','harihar']
#traverse
i=0
while i < len(names):
    print(names[i])
    i+=1

x=int(input("enter the number you want to search in tuple"))

num=(4,6,10,3,25,8,46,33)
j=0
while j < len(num):
    if(num[j]==x):
        print("Number found :",num[j],"at index :",j)
    j += 1
    

    
