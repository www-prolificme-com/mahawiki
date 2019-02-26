#By Abin Shoby
def find(l):	#calculates non repeating element
    ans=l[0]
    for i in range(1,len(l)):
        ans=ans ^ l[i]              #xoring will eliminate duplicate of a number
    return ans

print("Enter the Array (space separated):")
l=list(map(int, input().split(" ")))        #space separated entry
print("The non repeating value is:")
print(find(l))
