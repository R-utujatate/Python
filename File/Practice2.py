def check_for_line():
    word="learning"
    data=True
    line_no=1
    with open("practice.txt","r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return line_no
            line_no += 1
    return -1

check_for_line()


try:
    with open("practice.txt",'r') as f:
        longest_line=max(f,key=len)
    print("Longest line:")
    print(longest_line.strip())
except FileNotFoundError:
    print("File not found !")
except Exception as e:
    print(f"An error occurred: {e}")


file_path = "football_team.txt"

# Create file with captain and vice-captain
with open(file_path, 'w') as file:
    captain = input("Enter the name of the captain: ")
    vice_captain = input("Enter the name of the vice-captain: ")
    file.write(f"Captain: {captain}\nVice-Captain: {vice_captain}\n")

print("File created with captain and vice-captain.")

# Append team members
while True:
    member = input("Enter a team member's name (or type 'done' to finish): ")
    if member.lower() == 'done':
        break
    with open(file_path, 'a') as file:
        file.write(f"Member: {member}\n")
    print(f"{member} added to the team.")
