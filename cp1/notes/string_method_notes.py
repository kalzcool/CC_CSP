#CC string methods notes
sentance = "the quick brown fox jumps over the lazy dog"
# .strip()= removes white space, .title= first letter of each  word capital .capitalize=first letter first word .join= strings together .split=seperate lower=lowercase upper=uppercase .find=find what you wants num

word = input("what word do you want: ").strip().lower() 
new_word= input("What word should be in the sentence: ").strip().lower()

location= sentance.find(word) 
new_sentance= sentance.replace(word,new_word)
print(new_sentance)

first_name=input("what is your first name twinith: ").strip().title()
last_name=input("what is your last name twinith: ").strip().title()
first_seperated= first_name.split()
fixed= "".join(first_seperated)
last_seperated= last_name.split()
last_fixed= "".join(last_seperated)
full_name= fixed.title() + ' ' + last_fixed.title()
print("Hello "+ full_name.title())
print(full_name.isalpha)#checks its all letters
print(full_name.isnumeric)#checks for number
print(full_name.isupper)#uppercase



print(sentance.find("over"))
print(sentance.split('the'))

print(sentance.lower())
print(sentance.upper())
print(sentance.capitalize())
print(sentance.title())
print(fixed)
print(f"Hello {full_name.title()} welcome to my program")

letter=input("Give me a letter: ")
letter = letter[0].lower()
number_value =ord(letter)
number_value+= 2
new_letter= chr(number_value)
print(f"Your Letter was {letter} now it is {new_letter}")