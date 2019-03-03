# Ankit Tiwari
# 27/02/19
# Day 3	Write a function to count the occurence of all characters occuring in 2 given strings consisting of #
# assuming string is given in console letters only. For example, String 1 is "Surgical Strike" and string 2 is
# "by Indian Army" , it should print the occurence of every letter say S=2, U=1,R=3,G=1,I=4 etc.
# Using python3


def count_char(s_temp):
    Dict = {}
    for i in s_temp:
        if i in Dict.keys():
            Dict[i] += 1   # if found increment the value corresponding to key= i
        else:
            Dict[i] = 1  # add key i in dictonary with value 1
    return Dict


def main():
    s_input1 = input()
    s_input2 = input()
    s_temp = (s_input1 + s_input2).replace(" ", "") # only letter is to be counted so removing " "
    c_ans = count_char(s_temp)
    print(c_ans)


main()

