
# time complex O(n) memory O(n)
def find_most_occurring(string):
    #hash table to store count
    hash = {}
    ans = []
    for c in string:
        if c in hash:
            hash[c] += 1
        else:
            hash[c] = 1
    max = hash[string[0]]
    # if max is initialize to hash[string[0]] in case input is all characters appearing only once like "a b c d" 
    #output will be empty 
    # so initialize max to some min value like count can never be negative so initialize max = -1 or 0
    keys = hash.keys()
    for key in keys:
        if ( hash[key] > max):
            max = hash[key]
    
    for key in keys:
        if (hash[key] == max ):
            ans.append(key)

    return ans
    



#accept string
string = input()

print(find_most_occurring(string))
