import numpy as np

with open("Input.txt", "r") as f:
	line = f.readline().replace("\n", "")
	lines = []
	while line:
		lines.append(line)
		line = f.readline().replace("\n", "")

w, h = len(lines[0]), len(lines)

nums = np.zeros((w, h))
bestnum = -1
bestx, besty = -1, -1
for y in range(h):
	for x in range(w):
		if lines[x][y] == "#":
			angles = []
			for y2 in range(h):
				for x2 in range(w):
					ang = np.arctan2(y2 - y, x2 - x)
					if lines[x2][y2] == "#" and not (x2 == x and y2 == y) and not (True in np.isclose(angles, [ang] * len(angles))): # and not (np.arctan2(y2 - y, x2 - x) in angles):
						angles.append(ang)
			nums[x][y] = len(angles)
			if len(angles) > bestnum:
				bestx, besty = x, y
				bestnum = len(angles)

print(bestnum)