import numpy as np

with open("Input.txt", "r") as f:
	line = [i for i in f.readline().replace("\n", "")]
	lines = []
	while line:
		lines.append(line)
		line = [i for i in f.readline().replace("\n", "")]

w, h = len(lines), len(lines[0])

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

def getnextset(lines, x, y):
	angles = []
	next = []
	for y2 in range(h):
		for x2 in range(w):
			ang = np.arctan2(y2 - y, x2 - x)
			if lines[x2][y2] == "#" and not (True in np.isclose(angles, [ang] * len(angles))):
				angles.append(ang)
				next.append(((-ang + 3 * np.pi) % (2 * np.pi), x2, y2))
			elif lines[x2][y2] == "#" and (True in np.isclose(angles, [ang] * len(angles))):
				i = np.argmax(np.isclose(angles, [ang] * len(angles)))
				if (x2 - x) ** 2 + (y2 - y) ** 2 < (next[i][1] - x) ** 2 + (next[i][2] - y) ** 2:
					next[i] = ((-ang + 3 * np.pi) % (2 * np.pi), x2, y2)
	next.sort()
	return next

lines[bestx][besty] = "."

zaps = []
next = getnextset(lines, bestx, besty)
while len(next) > 0:
	for n in next:
		zaps.append((n[1], n[2]))
		lines[n[1]][n[2]] = "."
	next = getnextset(lines, bestx, besty)

if len(zaps) >= 200:
	print(zaps[199][1] * 100 + zaps[199][0])
else:
	print("TOO FEW")