def f(lis):
	for i in lis:
		if lis.count(i) == 1:
			return i
	else:
		return "No unique element found"

