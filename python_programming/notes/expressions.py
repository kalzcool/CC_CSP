#CC 7th expression notes

#algorithm example

name = input("What is your name:\n")
print("Hello", name)

#(pure torture guys) Treyson has 12 apples, he has 5 friends that he wants to give apples to. How many apples does each frin get? 
apples = 12
friends = 5
print("Each friend gets", apples/friends, "apples!")

# average age of a group of 4 friends
friend1 = 21
friend2 = 14
friend3 = 15
friend4 = 19 
total = friend1+friend2+friend3+friend4/4 
print("The average age between all of the friends is", total )

num1= int(input("tell me a number: \n"))
num2= float(input("Tell me another number: \n"))


num1 += num2
print("Addition(+): ", num1)
num1 -= num2
print("Subtraction(-): ", num1)
num1 *= num2 
print("Multiplication(*): ", num1)
num1 /= num2 
print("Division(/): " , round(num1, 2)) #keyword round (number to round, number of dicimal places)
num1 **= num2
print("Exponents(**): ", num1)
num1 //= num2
print("Interger Division(//): ", num1)
num1 %= num2
print("Modulo(%): ", num1)