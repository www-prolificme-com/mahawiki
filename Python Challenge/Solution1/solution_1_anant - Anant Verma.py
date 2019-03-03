#this is to take the input string of integers, split it into individual strings separated by whitespace and t
#then make them integer by mapping it and making it into a list of integers.
array = list(map(int, input().split()))

ele = array[0]
#by finding the XOR of all the numbers one by one, we get the number which is occurring only once in 
#the list
# in the above for loop code range is used which in Python 2 returns a list so unnecessary space is used
# and also indexing is used which is redundant 
# directly iterate over the array using  below code(line 16) 
# commenting your below code
#for i in range(1,len(array)): 
#    ele=ele^array[i]

ele = 0 # if i initialize ele to be array[0] then if array[0] is the element with count 1 it will print ans 0 never array[0]
for i in array:
    ele ^= i
#printing the unique number
print(ele)
