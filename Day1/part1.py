fuel = 0
with open("Input.txt", "r") as f:
	line = f.readline()
	while line:
		line = int(line)
		fuel += (line // 3) - 2
		line = f.readline()
print(fuel)