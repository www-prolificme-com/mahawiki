'''
Question 3: Given a range, print the output in the following fashion as given in the example. 
Range : 1 100 Print : 1 99 2 98 3 97 4 96 5 95 ...
'''
print("Enter the lower and upper range on separate lines.")
lower = int(input())
upper = int(input())
if (lower>upper):# comparing the bounds taken as input
    temp = lower
    lower = upper
    upper = temp
k = upper  # initializing temp
for i in range(lower, upper):# running loop from lower to upper
    k-=1# decrementing temp variable for desired output
    print(i, k, end=" ")# formatting output
