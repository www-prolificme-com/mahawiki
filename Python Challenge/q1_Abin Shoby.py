def find(l):
    ans=l[0]
    for i in range(1,len(l)):
        ans=ans ^ l[i]              #xoring will eliminate duplicate of a number
    return ans

#usage
#l=[1,1,2,2,3,4,4,5,5]
#print(find(l))
