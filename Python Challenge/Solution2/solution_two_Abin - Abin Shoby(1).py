def find(arr,sum1):
    ans=[]
    for i in range(0, len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == sum1:
                ans.append((arr[i],arr[j]))             #find each pair and check if their sum is equal to the given number
    for x in ans:
        print(x)

#usage
#arr=[1,2,5,3]
#sum1=3
#find(arr,3)
print("Enter the array (space separated):")
l=list(map(int, input().split(" "))) #space separated entry for array
print("Enter value of the  sum:")
n=int(input())  #accept value
print("The resultant pairs are:")
find(l,3)