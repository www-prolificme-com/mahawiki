'''
@author -> Aman Gupta
'''
from math import gcd
T = int(input())
for _ in range(T):
    a,b = map(int, input().split())
    ans = max(a,b)//gcd(a,b)
    print(ans)
