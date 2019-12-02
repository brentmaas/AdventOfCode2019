with open("Input.txt", "r") as f:
	line = f.readline().split(",")
	program = [int(i) for i in line]

#Additional puzzle thingy
program[1] = 12
program[2] = 2

print(program)

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
	
print(program)