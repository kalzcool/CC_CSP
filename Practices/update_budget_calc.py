#CC 7th updating financial calculator 

def monthly_amounts(income):
    income = float(input("What is your monthly income:"))
    rent = float(input("what is your monthly rent:"))
    utilities = float(input("utilities:"))
    groceries = float(input("groceries"))
    transportation = float(input("transportation"))
    savings = income*.1 
    spend = income -(utilities +rent +groceries +transportation + savings) 
    rent_percent = round(rent/income) *100 , 2
    utilities_percent = round (utilities/income) *100 , 2
    groceries_percent = round (groceries/income) *100 , 2
    transportation_percent = round (transportation/income) * 100 , 2
    savings_percent = round (savings/income) *100,2 
    spend_percent = round (spend/income) *100,2 
    

rent_percent = monthly_amounts(round(rent/income)*100,2)
utilities_percent = monthly_amounts(round(utilities/income)*100,2)
groceries_percent = monthly_amounts(round(groceries/income)*100,)
transportation_percent = monthly_amounts(round(transportation/income)*100,2)
savings_percent = monthly_amounts(round(savings/income)*100,2)
spend_percent = monthly_amounts(round(spend/income)*100,2)

print(f"\nYour rent is  and it is {rent_percent:.2f}% of your income")
print(f"\nYour utilities is ${utilities:.2f} it is {utilities_percent:.2f}% of your income") 
print(f"\nYour groceries is ${groceries:.2f} it is {groceries_perecent:.2f}%")
print(f"\nYour transportation is{transportation:.2f} is it {transportation_percent:.2f}%")
print(f"\nYour savings are {savings:.2f} it is {savings_percent}%")
print(f"\nYour amount to spend is {spend:.2f} it is {spend_percent}%") 
