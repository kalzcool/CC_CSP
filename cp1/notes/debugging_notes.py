#CC debugging notes

#syntax error
#print("Hello)
      
#indedtation 
#if True:
#print("blah blah)")

#logic error
apples = 20 
people = 3
print ( apples / people)
while True:
    try: 
        fav_num =int(input("What is your favorite num: "))
    except:
        print("that is not a number zawg")
    else:
        break 
print(4+ fav_num)