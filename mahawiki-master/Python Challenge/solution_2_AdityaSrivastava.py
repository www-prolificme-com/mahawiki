a=list(map(int,input().split()))
#same as question 1

#i was thinking of an O(n) solution but couldn't get and have other things to do so heres an O(n^2)
# pretty simple sloution

#first store all elements counts in a dictionary (initially 1)
# if we encounter any sum while looping we increase count by 1 
# and then print those keys whose count is greaater than 1

dicn={}
#dictionary to maintain count
for i in a:
        dicn[i]=1
    # set count to 1
n=len(a) #length of array
for i in range(n):
    for j in range(i): #since a+b = b+a we dont need to traverse the whole array till 'i' is enough
        x=(a[i]+a[j])
        if(x in dicn): #i.e. if sum is in array
            dicn[x]+=1
#print(dicn) #uncomment to see how the values are getting updated
for i in dicn.keys():
    if(dicn[i]>1): #simply printing the required elements
        print(i,sep=" ")
print()