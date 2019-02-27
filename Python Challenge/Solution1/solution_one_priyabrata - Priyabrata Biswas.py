# Python 3.6.7

def get_single_elem(input_list):
	new_list = []
	for item in input_list:
		new_list.remove(item) if (item in new_list) else new_list.append(item)
	return new_list[0]
# suppose the input is 1 2 3 4 5 6 7 8 .... 10^5 10^5 .... 8 7 6 5 4  3 2 1 0 # ans is 0
# line 5 will run for size 10^5 *2 + 1
# for each iteration if item in new_list is executed which in worst case is O(n) complexity if element to be found is the last
# if suppose its found remove operation will be executed which will be worst case O(n) if element to be deleted is first one
# worst case complexity of your program can be O(n^3) 
# instead use another data structure like map instead of new_list & just store item as key and corresponding count as value O(n)
# do above for each item total O(n^2)
# later sort the dict acc to value in ascending order O(nlogn) worst case and print value corresponding to 0th key
#O(n^3) will give TLE for input >= 10^3
# O(n^2) will work till 10^4
# if u want O(1) use xor
def main():
	input_list = input().split()
	res_elem = get_single_elem(input_list)
	print(res_elem)

main()
