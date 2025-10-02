#CC 7th updating financial calculator 

def monthly_amounts(other_things):
   return round(other_things/ income*100,2)

    
income= int(input("What is your monthly income\n"))

rent_percent = monthly_amounts(1500)
utilities_percent = monthly_amounts(600)
groceries_percent = monthly_amounts(100)
transportation_percent = monthly_amounts(85)


print(f"\nYour rent is {rent_percent}% of your income")
print(f"\nYour utilities  is {utilities_percent}% of your income") 
print(f"\nYour groceries is {groceries_percent}% of your income")
print(f"\nYour transportation is it {transportation_percent}% of your income")

#HOLY ANCIENTS I FIGURE IT OUT(HOPEFULLY) I MIGHT ACTUALLY CRY GUYS 