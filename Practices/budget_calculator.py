#CC 7th Budget calculator 

income = float(input("What is your monthly income:"))
rent = float(input("what is your monthly rent:"))
utilities = float(input("utilities:"))
groceries = float(input("groceries"))
transportation = float(input("transportation"))
savings = income*.1 
spend = income -(utilities +rent +groceries +transportation + savings) 
perecent_rent = rent/income*100 

rent_percent = (rent / income) * 100
utilities_percent = (utilities/income) *100
groceries_perecent = (groceries/income) *100
transportation_percent = (transportation/income) * 100
savings_percent = (savings/income) *100
spend_percent = (spend/income) *100


print(f"\nYour rent is ${rent:.2f} and it is {rent_percent:.2f}% of your income")
print(f"\nYour utilities are ${utilities:.2f} it is {utilities_percent:.2f}% of your income") 
print(f"\nYour groceries are ${groceries:.2f} it is {groceries_perecent:.2f}%")
print(f"\n")
print(f"\n")
print(f"\n")
