# Ankit Tiwari
# 25/02/19
# Day 2	Write a function to find all pairs in an integer array whose sum is equal to a given number.

# i am assuming the array and the specified number is taken as input from console
# my code will return only unique pairs of integer whose sum is equal to given number


def binary_search(arr, i, n, key):
    while i <= n:
        mid = (i + n) // 2
        if arr[mid] == key:
            return arr[mid]
        elif key > arr[mid]:
            i = mid+1
        else:
            n = mid - 1
    return None


def find_pairs(arr, key):
    ans = set()
    arr_len = len(arr)
    for i in range(arr_len-1):
        # find key-i in all remaining elements and add return element
        temp = binary_search(arr, i+1,arr_len-1, key-arr[i])
        if temp is None:
            continue
        else:
            ans.add((arr[i], temp))

    return ans


def main():
    arr = list(map(int, input().split())) # take input array
    key = int(input()) # specified number

    # naive soln will take o(n^2) as for each element we will traverse array till end to find whether a pair
    # exists whose sum is key
    # instead we can sort and then use binary search for each element to find whether a pair exists whose sum is key
    arr.sort() # nlog(n)
    solution = find_pairs(arr, key) # return set of tuples why set so that duplication is not allowed
    for i in solution:
        print(i)


main()
