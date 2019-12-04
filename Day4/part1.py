import numpy as np

#Input
low = 197487
high = 673251

def check(inp):
	a = str(inp)
	if not len(a) == 6:
		return 0
	valid = False
	for i in range(5):
		if int(a[i]) == int(a[i+1]):
			valid = True
		elif int(a[i]) > int(a[i+1]):
			return 0
	return 1 if valid else 0

n_valid = 0
for i in range(low, high+1):
	n_valid += check(i)
print(n_valid)