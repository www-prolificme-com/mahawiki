# Python 3.6.7

def get_single_elem(input_list):
	new_list = []
	for item in input_list:
		new_list.remove(item) if (item in new_list) else new_list.append(item)
	return new_list[0]

def main():
	input_list = input().split()
	res_elem = get_single_elem(input_list)
	print(res_elem)

main()
