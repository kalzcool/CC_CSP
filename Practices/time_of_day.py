#CC 7th getting the time of day

time = int(input("What is the time of day using military time?(00-24, hour only)\n"))

if time >= 20:
    print("Goodnight")
elif time <=20 and time >=18:
    print("Good evening") 
elif time <=17 and time >= 12:
    print("Good afternoon")
elif time <= 5:
    print("Go to bed, actually I'm a hypocrite continue on.")
else:
    print("Good moring")