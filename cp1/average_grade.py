#CC average grade calculator
#add try and execpt after confirming 
print("Hello, this is an automated GPA calculator, please answer the following questions of your grades until the second decimal point. Please note this calculator will skip whatever period you have lunch, move all classes down one to fill the space:")
one= float(input("What is your grade for first period: "))
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
two= float(input("What is your grade for second period: "))
three= float(input("What is your grade for third period: "))
four= float(input("What is your grade for fourth period: "))
five= float(input("What is your grade for fith period: "))
six= float(input("What is your grade for sixth period: "))
seven= float(input("What is your grade for seventh period: "))

gpa = (one+two+three+four+five+six+seven)/7
print("Here is your calculated gpa ", round(gpa, 2))