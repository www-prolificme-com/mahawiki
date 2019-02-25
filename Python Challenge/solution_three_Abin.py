def Counter(s):
	count={}
	for x in s:
		count[x]=0	#initialize the count dictionary
	for x in s:
		count[x]+=1	#calculate count of each character
	return count
		
def find(string):	#calculate most frequent character
    c = Counter(string)  #count of each character
    mx = max(c.values()) #maximum count value
    ind = list(c.values()).index(mx) #index of max value in dictionary
    print(list(c.items())[ind][0]) #take key of max value and the key is the required character
print("Enter the string:")
string=input().strip()
print("The most frequent character is:")
find(string)
