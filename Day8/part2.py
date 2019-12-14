import numpy as np
import matplotlib.pyplot as plt

w, h = 25, 6
with open("Input.txt", "r") as f:
	im = f.readline()

n = len(im) // w // h
image = np.array([int(i) for i in im]).reshape(n, h, w)

final_image = image[-1]
for i in range(1, n):
	j = n - i - 1
	for y in range(h):
		for x in range(w):
			final_image[y,x] = image[j,y,x] if not image[j,y,x] == 2 else final_image[y,x]

plt.figure()
plt.imshow(final_image)
plt.show()