# program to ask the user to enter names of their 3 favorite movies and store them in a list
movies=[]
mov1=input("enter 1st movie: ")
mov2=input("enter 2nd movie: ")
mov3=input("enter 3rd movie: ")

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)

print(movies)

#OR
movies.append(input("enter 4th movie : "))
movies.append(input("Enter 5th movie : "))
print(movies)
