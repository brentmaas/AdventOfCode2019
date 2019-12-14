import numpy as np

w, h = 25, 6
with open("Input.txt", "r") as f:
	im = f.readline()

n = len(im) // w // h
image = np.array([int(i) for i in im]).reshape(n, h, w)
curr_min = np.inf
curr_12 = None
for i in range(n):
	val, count = np.unique(image[i].flatten(), return_counts=True)
	d = dict(zip(val, count))
	try:
		if d[0] < curr_min:
			curr_12 = d[1] * d[2]
			curr_min = d[0]
	except:
		curr_12 = d[1] * d[2]
		break
print(curr_12)