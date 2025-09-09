#CC 7th string notes

#examples 
first_name = input("What is your first name: \n").strip().title() 

last_name = input("What is your last name:\n").strip().title()

full_name = first_name + " " + last_name 


sentance = 'the quick brown fox jumps over the lazy dog'.strip()
print(sentance.find("jumps"))
print(sentance[20:25])
print(sentance[sentance.find("lazy"): len("lazy")+sentance.find("lazy")])
print("Welcome to my program :3", full_name + "!")

# sanitization and stupid proofing

error = "This is a bug" 


numOne = "1"
numTwo = "2"

print("my favorite number is"+numOne)

