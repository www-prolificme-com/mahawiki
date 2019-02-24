s=input()
#input the string
dicn={}
#dictionary to maintain count
maxcount=0
#max count initializing

for i in s:
    if(i in dicn):
        dicn[i]+=1
    #if already in dicn then count is increased by1
    else:
        dicn[i]=1
    #else (i.e. it doesn't exist then set count to 1)
ans_array=[]
maxcount=max(dicn.values()) #finding the max count from all the values 
for i in dicn.keys():
    if(dicn[i]==maxcount):
        ans_array.append(i) #appending max count element/s to ans array

print(ans_array)