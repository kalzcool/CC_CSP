#CC 7th fizzbuzz

n = 1 

while n <51:
    if  n % 15 ==0:
        print("fizzbuzz")
    elif n % 5 == 0:
        print("buzz")
    elif n % 3 == 0:
        print("fizz")
    else:
        print(f"{n}")
    n += 1