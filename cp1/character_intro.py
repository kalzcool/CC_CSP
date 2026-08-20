#CC character intro
import time 

choice = input("Would you like to learn about Desmendova, or Rae? ")
time.sleep(.25)
if choice == "Desmendova":
    d_name= "Desmendova"
    d_age = "17"
    d_job = "REDACTED"
    d_from = "Amity park"
    print("This canidates name is " +d_name+ " Age " +d_age+ " Previous work experience " +d_job+ " They were raised in "+d_from)

    answer = input("Does this canidate intrest you: ")
    time.sleep(1)
    if answer == "Yes":
        print("Understood")
    else:
        print("Onto the next then")
        time.sleep(.25)
elif choice == "Rae":
    r_name= "Rae"
    r_age = "16"
    r_job = "Peer tutor"
    r_from = "Salem"
    print("This canidates name is " +r_name+ " Age " +r_age+ " Previous work experience " +r_job+ " They were raised in "+r_from)
    answer = input("Does this canidate intrest you: ")
    time.sleep(1)
    if answer == "Yes":
        print("Understood")
    else:
        print("Onto the next then")
else:
    print("That is not a valid answer")
    time.sleep(.25)