#CC idiot proof 
name =input("What is your full name: ").strip().title()
while True:
    try:
        phone=int(input("What is your phone number: "))
        new_phone=phone.split()
        phone_format= " ".join(new_phone)
        print(phone_format)
    except:
        print("Nope try again")
    else:
        break
while True:
    try:
        gpa=float(input('What is your gpa: '))
    except:
        print("Nope try again")
    if gpa >=5.1:
        raise Exception("Nice try ")
    else:
        break



print(f"Hello {name}, your phone number is: {phone}, your gpa is {round(gpa, 2)}")