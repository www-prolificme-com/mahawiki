from collections import Counter
def f(s):
	res = Counter(s.lower())
	print(res.most_common(1))

Example:

s = "abhiAbhiaaaa"

f(s)
[('a', 6)]