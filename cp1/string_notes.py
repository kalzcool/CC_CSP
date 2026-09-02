#CC string notes
name = "cal"
age="15"
print(age + "2")
print( name + " " + age)
#escape cahracter: \ . \n = new line, \t = tab line
sentence= 'then he said \n "That isn\'t fair"'
print(sentence)
print("*" * 30)
sentance = "The quick brown fox jumps over the lazy dog" 
print(sentance)
print(sentance.find("f"))
word =input("what word do you want; ") 
start = sentance.find(word)
length=len(word)
print(sentance[start: start+length])