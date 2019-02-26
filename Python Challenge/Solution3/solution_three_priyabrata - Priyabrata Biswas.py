# Python 3.6.7

import operator

def max_occur(input_str):
	record = {}
	for char in input_str:
		if char in record:
			record[char] += 1;
		else:
			record[char] = 1
	max_val = max(record.values())
	res = [key for key in record.keys() if record[key] == max_val]
	return res[0] if (len(res) == 1) else res

def main():
	input_str = input()
	res_elem = max_occur(input_str)
	print(res_elem)

main()
