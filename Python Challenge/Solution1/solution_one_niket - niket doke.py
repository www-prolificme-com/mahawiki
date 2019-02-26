
# time complex O(n) memory O(n) program assumes the array element has only 1 unique element
def find_unqiue_element(arr):
    #hash table to store count
    hash = {}
    # iterate through array
    for e in arr:
        if e in hash :
            hash[e]+=1
        else:
            hash[e] = 1
    
    for key in hash.keys():
        if hash[key] == 1:
            return key
    # any chance wrong input
    return None 


#array length redandent
n = int(input())
#array input
arr = list(map(int,input().split()))

ans = find_unqiue_element(arr)
if( ans == None):
    print("Wrong input")
else:
    print(ans)


