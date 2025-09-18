#CC 7th old enough 

age = int(input("What is your age?\n"))

if age >= 18:
    print("You are old enought to vote") 
elif age >= 16 and not age > 18:
    print("You are old enough to drive") 
elif age >= 15 and not age > 16:
    print("You can get your learners permit")
elif age >=4 and not age > 15:
    print("You are old enough to go to school")
else:
    print("You are too young for anything")