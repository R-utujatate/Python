'''
Break : used to terminate the loop when encountered
Continue : terminates execution in the current iteration & continues execution 
of the loop with the next iteration.
'''
num=(1,2,3,4,6,5,7,5,8)
x=7
i=0
while num[i]<len(num):
    if(num[i]==x):
        print("found")
        break
    i += 1

print("end of loop")

i=0
while i <= 5:
    if(i==3):
       i+=1
       continue
    print(i)
    i+=1

print("Print all odd number from 1 to 20")
j=1
while j <= 20:
    if(j%2==0):
        j+=1
        continue
    print(j)
    j+=1
    

    


