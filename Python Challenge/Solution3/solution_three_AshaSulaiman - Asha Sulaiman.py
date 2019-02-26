userInput=input()
my_input=list(userInput)

count= {}
 
for char in my_input:
 count[char] = count.get(char,0)+1
m=max(count,key=count.get)

print(m)  