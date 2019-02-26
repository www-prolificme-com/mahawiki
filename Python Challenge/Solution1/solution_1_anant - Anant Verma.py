#this is to take the input string of integers, split it into individual strings separated by whitespace and t
#then make them integer by mapping it and making it into a list of integers.
array = list(map(int, input().split()))

ele = array[0]
#by finding the XOR of all the numbers one by one, we get the number which is occurring only once in 
#the list
for i in range(1,len(array)):
    ele=ele^array[i]
#printing the unique number
print(ele)
