# python 3
# Given a range, print the output in the following fashion as given in the example
# Range : 1 100 Print : 1 99 2 98 3 97 4 96 5 95 ...
# time complexity O(n-m)

def main():
    m, n = map(int, input().split())
    for i in range(m, n+1):
        print(i, n-i)


main()
