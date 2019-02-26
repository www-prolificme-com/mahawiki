# time complex O(n) memory O(n)
def find_allpairs(arr,k):
    #hash table to store numbers
    hash = {}
    ans = []
    for i in range(len(arr)):
        #check if complement of arr[i] wrt sum is in hash if yes we have pair else no
        if ( (k - arr[i]) in hash):   
            ans.append([(k-arr[i]),arr[i]])
        else:
            hash[arr[i]] = i
    return ans
        



#array length and sum
n , k = list(map(int,input().split()))
#array input
arr = list(map(int,input().split()))

ans = find_allpairs(arr,k)

print(ans)