import copy

with open("Input.txt", "r") as f:
	line = f.readline().split(",")
	program = [int(i) for i in line]

#Additional puzzle thingy
program[1] = 12
program[2] = 2

def computer(program, noun, verb):
	program[1] = noun
	program[2] = verb
	p = 0
	while True:
		if program[p] == 1: #Add
			program[program[p+3]] = program[program[p+1]] + program[program[p+2]]
			p += 4
		elif program[p] == 2: #Mult
			program[program[p+3]] = program[program[p+1]] * program[program[p+2]]
			p += 4
		elif program[p] == 99: #Exit
			break
	return program[0]

target = 19690720

for i in range(99):
	for j in range(99):
		if computer(copy.copy(program), i, j) == target:
			print(100 * i + j)
			exit()