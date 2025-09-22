#CC 7th loops notes

foods= ["Chocolate","Pasta" , "Brownies", "Cookies", "Nutela", "Candy"]

#for loops
for food in foods:
    #rint(f"{food} is my favorite food")
    print("Hi!")

for x in range(1,20):
    print(x)


#while loops
#1, iterator= how many times loop has run
#2 set stopping point
#3 increase iterator
 # 
#hle True:
    #pint(i)
   #i+=1""

#Infinte loop (one of 3 steps missing)

#correct while loop

i = 1

while i<20:
    print(i)
    i += 1 

x = 1

while x<21:
    if x % 2==0:
        print(f"{x} is an even number")
    else:
         print(f"{x} is an odd number")
    x += 1

import random

d = 1
end = random.randint(1,20)

#hile d != end:
  # print("Duck") 
   #d+= 1

#rint("goose")

while True:
    if d == end:
        print("Goose!")
        break
    else:
        print("Duck")
        d +=1