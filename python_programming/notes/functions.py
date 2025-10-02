#CC 7th Functions notes

def welcome():
    name = input("What is your name?")
    print(f"Hello, {name}!") 

print("This is not in my function")

#welcome()
#welcome()
#welcome()
#welcome()

def add(number, number_two):
    number += num_two 
    print(number)

num_one = 12 
num_two = 4 

#add(80, 8)
#add(3, 6)
#add(9, 20)
#add(11, 71)
#add(num_one, num_two)

import random 

def roll(mod):
    return random.randint(2, 18) + mod

strength = roll(0)
dextarity = roll(1)
intellegence = roll(1) 
charisma = roll(0)
print("Here are your stats!")
print(f"strength: {strength}\nDex: {dextarity}\nInt: {intellegence}\nChar: {charisma}") 