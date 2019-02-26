arr = [1, 1, 2, 2, 3, 4, 4, 5, 5] # input array to process 
min = 1 # setting the min index to 1 for searching 
for i in arr: # looping through the array
    if arr.count(i) == min: # check if the count of i'th data in array is equal to the value of min 
        data = i # setting the value of data to the i'th data that satisfies above condition
print(data) # printing the output
