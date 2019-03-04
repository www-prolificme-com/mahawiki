# Ankit Tiwari
# 28/02/19
# Pyhton 3
# Given an array of 99 integers between 1-100, find the nmissing integer. No integer is repeated and only
# one integer is missing. (Preferably do it in a single pass,or max. 3 passes) (Code must be most optimised,
# for time and space complexity.
# O(n) complexity worst case


def main():
    i_arr = set(map(int, input().split()))
    for i in range(1, 101):
        if i not in i_arr: # O(1) operation as set is implemetes as hash table and literally no chance of collision
            # as only 100 elements are present
            print(i)
            break


main()


