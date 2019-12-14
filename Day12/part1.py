import numpy as np

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
n = 1000

for t in range(n):
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

e = 0
for i in range(len(x)):
	print(f"pos=<x={x[i]}, y={y[i]}, z={z[i]}>, vel=<x={vx[i]}, y={vy[i]}, z={vz[i]}>")
	e += (abs(x[i]) + abs(y[i]) + abs(z[i])) * (abs(vx[i]) + abs(vy[i]) + abs(vz[i]))
print(f"Energy: {e}")