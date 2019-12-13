import numpy as np
import copy

x, y, z = [], [], []
with open("Input.txt", "r") as f:
	line = f.readline()
	while line:
		l = line.replace("\n", "").replace(">", "").replace("<", "").replace("x=", "").replace("y=", "").replace("z=", "").split(", ")
		x.append(int(l[0]))
		y.append(int(l[1]))
		z.append(int(l[2]))
		line = f.readline()
vx, vy, vz = [0] * len(x), [0] * len(y), [0] * len(z)

sx, sy, sz = copy.copy(x), copy.copy(y), copy.copy(z)

tx, ty, tz = None, None, None
t = 0
while None in [tx, ty, tz]:
	for i in range(len(x)):
		for j in range(len(x)):
			if not i == j:
				vx[i] += 1 if x[i] < x[j] else -1 if x[i] > x[j] else 0
				vy[i] += 1 if y[i] < y[j] else -1 if y[i] > y[j] else 0
				vz[i] += 1 if z[i] < z[j] else -1 if z[i] > z[j] else 0
	for i in range(len(x)):
		x[i] += vx[i]
		y[i] += vy[i]
		z[i] += vz[i]
	t += 1
	if tx is None and np.all(np.array(x) == np.array(sx)) and np.all(np.array(vx) == np.zeros(len(vx))):
		tx = t
		print(f"X: {t}")
	if ty is None and np.all(np.array(y) == np.array(sy)) and np.all(np.array(vy) == np.zeros(len(vy))):
		ty = t
		print(f"Y: {t}")
	if tz is None and np.all(np.array(z) == np.array(sz)) and np.all(np.array(vz) == np.zeros(len(vz))):
		tz = t
		print(f"Z: {t}")
print(np.lcm.reduce(np.array([tx, ty, tz]).astype(np.int64)))