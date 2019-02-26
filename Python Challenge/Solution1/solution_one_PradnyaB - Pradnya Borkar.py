#input= 1,1,2,2,3,4,4,5,5
#ouput: 3
array=list(map(int,input("Enter Array").split(',')))
arr=set(array)
for i in arr:
	if array.count(i)==1:
		print(i)
		break;
"""
>>>python solution_one_PradnyaB.py
1,1,2,2,3,4,4,5,5,6,6
3
>>>python solution_one_PradnyaB.py
1,2,2
1