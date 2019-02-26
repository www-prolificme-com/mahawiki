# Ankit Tiwari
# 25/02/19
# Day 3	Write a function to return most occuring character in a String.
# assuming string is given in console
# Using python3


def most_recurring_1(s_input):
    Dict = {}
    for i in s_input:
        if i in Dict.keys():
            Dict[i] += 1   # if found increment the value corresponding to key= i
        else:
            Dict[i] = 1  # add key i in dictonary with value 1

    sorted_dict = sorted(Dict.items(), key=lambda char_value: char_value[1], reverse=True)
    # sorted_dict contains list of tuples sorted by values of key in descending order because reverse is set to
    # true

    print(sorted_dict)
    return sorted_dict[0][0] # sorted_dict[0] is tuple sorted_dict[0][0] is first element of 0th tuple


def main():
    s_input = input()
    c_ans = most_recurring_1(s_input) # without using collection
    print(c_ans)


main()
