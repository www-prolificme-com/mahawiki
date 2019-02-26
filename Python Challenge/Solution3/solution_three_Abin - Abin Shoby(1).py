from collections import Counter

def find(string):
    c = Counter(string)  #count of each character
    mx = max(c.values()) #maximum count value
    ind = list(c.values()).index(mx) #index of max value in dictionary
    print(list(c.items())[ind][0]) #take key of max value

#usage
#string=‘aaaaaaaaaaaaaaaaaabbbbcddddeeeeee’
#find(string)
print("Enter the string:")
string=input().strip()
print("The most frequent character is:")
find(string)