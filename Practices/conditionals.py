#CC 7th conditonals notes

#homework_done = input("is your homework done: ").strip().capitalize()

#if homework_done == "No":
#    print("Then go do your homework.")
#else:
  #  print("Yes you can go")


name = input("What is your name?:\n") 
if name == "Ms LaRose":
    print("You are the Teacher")
elif name == "Tia" or name == "Ashley":
    print("You are the TA")
else:
    print(f"Hello {name}, you are a student")
     
grade = 157

if grade >=90:
    if grade > 100:
        print("You cheated, that is not possible")
    else:
        print(f"You have {grade}% that is an A :3") 
elif grade >= 80 and not grade > 100: 
    print(f"You have {grade}% that is a B")
elif grade >= 70 and not grade > 100:
    print(f"you have a {grade}% that is a c")
else: 
    print(f"You have a {grade}% that is so far from an A.. How did you even get that.?")





