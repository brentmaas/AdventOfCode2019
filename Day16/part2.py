import numpy as np

with open("Input.txt", "r") as f:
	inp = [int(i) for i in f.readline().replace("\n", "")]

N = 100
repeat = 10000

offset = sum([inp[i] * 10 ** (6 - i) for i in range(7)])
inp = np.array((inp * repeat)[offset:])

for _ in range(N):
	inp = (abs(np.cumsum(inp[::-1])) % 10)[::-1]

print(inp[:8])