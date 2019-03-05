'''
Question 2: Write a function to count the occurence of all characters occuring in 2 given 
strings consisting of letters only. For example, String 1 is "Surgical Strike" and string 2 is 
"by Indian Army", it should print the occurence of every letter say S=2, U=1,R=3,G=1,I=4 etc.
'''
characters = []
counter = []
distinct = {}
string1 = input("Enter String 1: ")
string2 = input("Enter String 2: ")
# taking two string inputs and 
# populating the lists predefined with the characters in the string
for i in string1.upper().replace(" ", ""):
    characters.append(i)
    counter.append(1)
for j in string2.upper().replace(" ", ""):
    characters.append(j)
    counter.append(1)
#print(characters)
#print(counter)
# combining the two lists into one dictionary and
# thus weeding out repetitions and counting the occurrences
for k in range(0,len(characters)):
    if characters[k] in distinct:
        distinct[characters[k]] += counter[k]
    else:
        distinct[characters[k]] = counter[k]
# formatting output as needed
count = 0
for key, value in distinct.items():
    print(str(key)+ "=" + str(value),end="")
    count+=1
    if (count < len(distinct)):
        print(", ", end="")
