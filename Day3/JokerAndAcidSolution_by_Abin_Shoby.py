from fractions import Fraction
t=int(input())
for tt in range(t):
    n,m=map(int,input().split(" "))
    print((Fraction(min(n,m), max(n,m))).denominator)
