'''
Question 1: Given an array of 99 integers between 1-100, find the nmissing integer. 
No integer is repeated and only one integer is missing. 
(Preferably do it in a single pass,or max. 3 passes) 
(Code must be most optimised, for time and space complexity.
'''
import random
# Generating array
#arr = []
#for i in range(1,101):
#    arr.append(i)
#print(arr) 

# Shuffling array
#arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
#random.shuffle(arr)
#print(arr)

# deleting randomly from array
#arr = [39, 38, 83, 94, 72, 56, 17, 68, 97, 92, 8, 40, 1, 42, 21, 30, 27, 7, 45, 31, 20, 6, 62, 33, 34, 98, 22, 48, 41, 88, 95, 89, 13, 46, 50, 29, 54, 80, 19, 70, 86, 55, 59, 87, 71, 3, 93, 43, 12, 85, 53, 58, 67, 73, 63, 37, 26, 35, 61, 81, 15, 52, 57, 36, 74, 10, 11, 28, 64, 5, 14, 16, 84, 69, 79, 91, 82, 77, 60, 76, 100, 24, 4, 99, 47, 32, 65, 78, 9, 23, 66, 75, 90, 25, 18, 44, 49, 51, 96, 2]
#del arr[28]
#print(arr)
#print(len(arr))

# Actual Code
arr = [39, 38, 83, 94, 72, 56, 17, 68, 97, 92, 8, 40, 1, 42, 21, 30, 27, 7, 45, 31, 20, 6, 62, 33, 34, 98, 22, 48, 88, 95, 89, 13, 46, 50, 29, 54, 80, 19, 70, 86, 55, 59, 87, 71, 3, 93, 43, 12, 85, 53, 58, 67, 73, 63, 37, 26, 35, 61, 81, 15, 52, 57, 36, 74, 10, 11, 28, 64, 5, 14, 16, 84, 69, 79, 91, 82, 77, 60, 76, 100, 24, 4, 99, 47, 32, 65, 78, 9, 23, 66, 75, 90, 25, 18, 44, 49, 51, 96, 2]
num = 0
try:
    for i in range(1,101):# iterating through the range
        num = i
        arr.index(num)# will throw exception if i not found in array
except:
    print("Missing Number:",num) #catching the number missing
