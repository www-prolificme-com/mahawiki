a = list(map(int,input().split()))
# standard one liner to input an array in python
# I recommend to just use it or learn it if a beginner or too lazy to google 
# the usage of map()
# map is a function used to store the output of the whole list when iterated through a function without any actual iteration happened.
# simple explanation.., loop can be done in a single line with the help of map function.

# every element is repeated twice except one we need to find that
# XOR is the ans 
# a^a =0 
# so if we XOR every element which is repeated twice XOR will give a 0
# and 0 ^ a = a
ans = 0
for i in a: # looping through the array
    ans^=i
# XOR all the elements
# print ans
print(ans)
