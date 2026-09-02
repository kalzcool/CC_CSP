#CC average grade calculator
#add try and execpt after confirming 
print("Hello, this is an automated GPA calculator, please answer the following questions of your grades until the second decimal point. Please note this calculator will skip whatever period you have lunch, move all classes down one to fill the space:")

while True:
    try: 
       one= float(input("What is your grade for first period: "))
    except:
        print("that is not a number zawg")
    else:
        break 

if one >=94:
    one= 4.0
elif one <= 93 and one >=90:
    one=3.7
elif one <=89 and one>=87:
    one=3.3
elif one <=86 and one >=83:
    one= 3.0
elif one <=82 and one>=80:
    one=2.7
elif one <=79 and one>=77:
    one=2.3
elif one <=76 and one>=73:
    one=2.0
elif one <=72 and one>=70:
    one=1.7
elif one <=69 and one>=67:
    one=1.3
elif one <=62 and one>=60:
    one=0.7
else: 
    one=0.0
while True:
    try: 
       two= float(input("What is your grade for second period: "))
    except:
        print("that is not a number zawg")
    else:
        break 
if two >=94:
    two= 4.0
elif two <= 93 and two >=90:
    two=3.7
elif two <=89 and two>=87:
    two=3.3
elif two <=86 and two >=83:
    two= 3.0
elif two <=82 and two>=80:
    two=2.7
elif two <=79 and two>=77:
    two=2.3
elif two <=76 and two>=73:
    two=2.0
elif two <=72 and two>=70:
    two=1.7
elif two <=69 and two>=67:
    two=1.3
elif two <=62 and two>=60:
    two=0.7
else: 
    two=0.0
while True:
    try: 
       three= float(input("What is your grade for third period: "))
    except:
        print("that is not a number zawg")
    else:
        break 
if three >=94:
    three= 4.0
elif three <= 93 and three >=90:
    three=3.7
elif three <=89 and three>=87:
    three=3.3
elif three <=86 and three >=83:
    three= 3.0
elif three <=82 and three>=80:
    three=2.7
elif three <=79 and three>=77:
    three=2.3
elif three <=76 and three>=73:
    three=2.0
elif three <=72 and three>=70:
    three=1.7
elif three <=69 and three>=67:
    three=1.3
elif three <=62 and three>=60:
    three=0.7
else: 
    three=0.0
while True:
    try: 
       four= float(input("What is your grade for fourth period: "))
    except:
        print("that is not a number zawg")
    else:
        break 
if four >=94:
    four= 4.0
elif four <= 93 and four >=90:
    four=3.7
elif four <=89 and four>=87:
    four=3.3
elif four <=86 and four >=83:
    four= 3.0
elif four <=82 and four>=80:
    four=2.7
elif four <=79 and four>=77:
    four=2.3
elif four <=76 and four>=73:
    four=2.0
elif four <=72 and four>=70:
    four=1.7
elif four <=69 and four>=67:
    four=1.3
elif four <=62 and four>=60:
    four=0.7
else: 
    four=0.0
while True:
    try: 
       five= float(input("What is your grade for fifth period: "))
    except:
        print("that is not a number zawg")
    else:
        break 
if five >=94:
    five= 4.0
elif five <= 93 and five >=90:
    five=3.7
elif five <=89 and five>=87:
    five=3.3
elif five <=86 and five >=83:
    five= 3.0
elif five <=82 and five>=80:
    five=2.7
elif five <=79 and five>=77:
    five=2.3
elif five <=76 and five>=73:
    five=2.0
elif five <=72 and five>=70:
    five=1.7
elif five <=69 and five>=67:
    five=1.3
elif five <=62 and five>=60:
    five=0.7
else: 
    five=0.0
while True:
    try: 
       six= float(input("What is your grade for sixth period: "))
    except:
        print("that is not a number zawg")
    else:
        break 
if six >=94:
    six= 4.0
elif six <= 93 and six >=90:
    six=3.7
elif six <=89 and six>=87:
    six=3.3
elif six <=86 and six >=83:
    six= 3.0
elif six <=82 and six>=80:
    six=2.7
elif six <=79 and six>=77:
    six=2.3
elif six <=76 and six>=73:
    six=2.0
elif six <=72 and six>=70:
    six=1.7
elif six <=69 and six>=67:
    six=1.3
elif six <=62 and six>=60:
    six=0.7
else: 
    six=0.0
while True:
    try: 
       seven= float(input("What is your grade for seventh period: "))
    except:
        print("that is not a number zawg")
    else:
        break 
if seven >=94:
    seven= 4.0
elif seven <= 93 and seven >=90:
    seven=3.7
elif seven <=89 and seven>=87:
    seven=3.3
elif seven <=86 and seven >=83:
    seven= 3.0
elif seven <=82 and seven>=80:
    seven=2.7
elif seven <=79 and seven>=77:
    seven=2.3
elif seven <=76 and seven>=73:
    seven=2.0
elif seven <=72 and seven>=70:
    seven=1.7
elif seven <=69 and seven>=67:
    seven=1.3
elif seven <=62 and seven>=60:
    seven=0.7
else: 
    seven=0.0
gpa = (one+two+three+four+five+six+seven)/7
print("Here is your calculated gpa ", round(gpa, 2))