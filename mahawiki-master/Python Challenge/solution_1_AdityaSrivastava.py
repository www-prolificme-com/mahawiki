a=list(map(int,input().split()))
#standard one liner to input an array in python
# i recommend to just use it or learn it if a beginner or too lazy to google 
# the usage of map()

# every element is repeated twice except one we need to find that
# exor is the ans 
# a^a =0 
# so if we exor every element which is repeated twice exor will give a 0
# and 0 ^ a = a
ans=0
for i in a: #looping through the array
    ans^=i
#exor all the elements
#print ans
print(ans)