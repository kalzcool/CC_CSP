#CC unit one final project 

print("Hello, this is an automated response, I am here to help you build an introduction of yourself for whatever your heart desires. Please answer the following questions accordingly so I may be of the best assistance to you today.")

u_name=input("What is your name? ")
u_age=input("How old are you? ")
u_hair_color=input("What color is your hair? ")
u_hobby=input("What is your main hobby? ")
if u_hobby == "Nothing".lower() or u_hobby == "None".lower():
	print("You’re a big bum")
else:
	print("nice")

u_job=str(input("Do you have a job? ")).lower()
if u_job == "yes":
	print("alright")
else:
	print("loser…")
u_bug=input("What is your favorite bug? ")

print("Here is your intro, " +u_name)
print("Hello, my name is " +u_name+ ". I am " +u_age+ " years old. I have " +u_hair_color+ " hair. My main hobby is "+u_hobby+ " Do I have a job currently? The answer is " +u_job+ " My favorite bugs are, " +u_bug+ ". I’m excited to be here.")
