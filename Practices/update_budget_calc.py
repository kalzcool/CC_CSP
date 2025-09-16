#CC 7th updating financial calculator 

income = float(input("What is your monthly income:"))
rent = float(input("what is your monthly rent:"))
utilities = float(input("utilities:"))
groceries = float(input("groceries"))
transportation = float(input("transportation"))

def monthly_amounts(income):
   

income*.1 
spend = income -(utilities +rent +groceries +transportation + savings) 
perecent_rent = rent/income*100 
rent_percent = (rent / income) * 100
utilities_percent = (utilities/income) *100
groceries_perecent = (groceries/income) *100
transportation_percent = (transportation/income) * 100
savings_percent = (savings/income) *100
spend_percent = (spend/income) *100


print(f"\nYour rent is ${rent:.2f} and it is {rent_percent:.2f}% of your income")
print(f"\nYour utilities is ${utilities:.2f} it is {utilities_percent:.2f}% of your income") 
print(f"\nYour groceries is ${groceries:.2f} it is {groceries_perecent:.2f}%")
print(f"\nYour transportation is{transportation:.2f} is it {transportation_percent:.2f}%")
print(f"\nYour savings are {savings:.2f} it is {savings_percent}%")
print(f"\nYour amount to spend is {spend:.2f} it is {spend_percent}%")