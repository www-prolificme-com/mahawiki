String1=input("Enter String")
list1=list(String1)
set1=set(list1)
maximum=0
val=""
for i in set1:
	if maximum<list1.count(i):
		maximum=list1.count(i)
		val=i
print(val)
"""
Enter String aaaaaaaaaaaaaaaaaabbbbcddddeeeeee
a
"""