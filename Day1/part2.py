fuel = 0
with open("Input.txt", "r") as f:
	line = f.readline()
	while line:
		line = int(line)
		fuel += (line // 3) - 2
		dfuel = (((line // 3) - 2) // 3) - 2
		while dfuel > 0:
			fuel += dfuel
			dfuel = (dfuel // 3) - 2
		line = f.readline()
print(fuel)