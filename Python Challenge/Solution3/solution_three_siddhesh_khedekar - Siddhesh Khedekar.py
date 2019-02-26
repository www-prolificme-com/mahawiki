str = input()  # input the string to process
max = 0  # setting the max variable to 0
for i in str:  # looping through the array
    if str.count(i) > max:  # check if the count of i'th data in the string is greater than the value of max
        data = i  # setting the value of data to the i'th data that satisfies above condition
        max = str.count(i) # setting the value of max to the count of i'th data that satisfies above condition
print(data)  # printing the output
