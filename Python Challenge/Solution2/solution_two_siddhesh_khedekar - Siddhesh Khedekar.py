arr = [1, 1, 2, 2, 3, 4, 4, 5, 5] # input array to process
n = len(arr) # calculating the length of the array
sum = 5 # setting the sum for calculating
pairs = [] # initializing the list fro
for i in range(0, n):  # looping through the array 0 - n
    for j in range(i + 1, n):  # looping through the array i+1 - n
        if arr[i] + arr[j] == sum: # consider all possible pairs and check their sums
            pairs.append([arr[i], arr[j]]) # populate the output list of pairs
print(pairs)  # printing the output
