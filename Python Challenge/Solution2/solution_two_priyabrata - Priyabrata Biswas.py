# Python 3.6.7

def find_pair(input_list, sum):
	new_list = []
	res_list = []
	for item in input_list:
		item = int(item)
		comp = sum - item
		if comp in new_list:
			res_list.append([comp, item])
			new_list.remove(comp)
		else:
			new_list.append(item)
	return res_list

def main():
	input_list = input().split()
	sum = int(input())
	res_list = find_pair(input_list, sum)
	print(res_list)

main()
