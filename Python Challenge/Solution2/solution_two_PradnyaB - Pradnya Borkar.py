#Write a function to find all pairs in an integer array whose sum is equal to a given number.
"""input: 2,4,1,5,3,6,7,8,9,10
		  6
"""
outputList=[]
array=list(map(int,input("Enter Array:").split(',')))
number=int(input("Enter a number"))
for i in range(len(array)):
	for j in range(i+1,len(array)):
		if array[i]+array[j] == number :
			outputList.append([array[i],array[j]])
print("All pairs in an integer array whose sum is equal to a given number is:\n",outputList)
"""
Enter Array:1,2,3,4,5,6,7,8,9,3
Enter a number6
All pairs in an integer array whose sum is equal to a given number is:
 [[1, 5], [2, 4], [3, 3]]
"""