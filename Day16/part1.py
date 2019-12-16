with open("Input.txt", "r") as f:
	inp = [int(i) for i in f.readline().replace("\n", "")]

N = 100
base_pattern = [0, 1, 0, -1]

for i in range(N):
	outp = [0] * len(inp)
	for j in range(len(inp)):
		pattern = []
		for k in base_pattern:
			pattern += [k] * (j + 1)
		pattern *= len(inp)
		pattern = pattern[1:len(inp)+1]
		outp[j] = abs(sum([pattern[k] * inp[k] for k in range(len(inp))])) % 10
	inp = outp

print(inp[:8])