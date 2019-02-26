# Ankit Tiwari
# 25/02/19
# Python 3
# Day 1	There is an array with every element repeated twice except one. Write a function to find that element.
# i am assuming the array will be the input from console


def find_key_count_one(arr):
    dict_arr = {}
    for i in arr:
        if i in dict_arr.keys():
            dict_arr[i] += 1  # if found increment the value corresponding to key= i
        else:
            dict_arr[i] = 1  # add key i in dictonary with value 1

    dict_arr_sorted = sorted(dict_arr.items(), key= lambda num_count: num_count[1])
    # sorted return list of tuples(key value pair) sorted according to value of key in ascending order
    return dict_arr_sorted[0][0]  # 0th tuple is ans and 0th element of tuple is the key


def main():
    arr = list(map(int, input().split()))  # take input from console and store it in a list
    ans = find_key_count_one(arr)
    print(ans)


main()

