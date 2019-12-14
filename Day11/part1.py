import io
import sys
import numpy as np

with open("Input.txt", "r") as f:
	line = f.readline().split(",")
	program = [int(i) for i in line]

def getargs(program, p, modes, argc, relative_base):
	args = []
	for i in range(argc):
		if len(modes) >= i + 1 and not modes[i] == 0:
			if modes[i] == 1:
				args.append(p + i + 1)
			elif modes[i] == 2:
				args.append(program[p + i + 1] + relative_base)
		else:
			args.append(program[p + i + 1])
	return args

def computer(program, noun=None, verb=None, stdin=sys.stdin, stdout=sys.stdout, returnonwrite=False, state=0, base_state=0):
	if not noun is None:
		program[1] = str(noun)
	if not verb is None:
		program[2] = str(verb)
	p = state
	relative_base = base_state
	buffer = []
	while True:
		opcode = int(str(program[p])[-min(2, len(str(program[p]))):])
		if len(str(program[p])) > 2:
			modepart = str(program[p])[:len(str(program[p]))-2][::-1]
			modes = [int(modepart[i]) for i in range(len(modepart))]
		else:
			modes = []
		if opcode == 1: #Add
			args = getargs(program, p, modes, 3, relative_base)
			program[args[2]] = program[args[0]] + program[args[1]]
			p += 4
		elif opcode == 2: #Mult
			args = getargs(program, p, modes, 3, relative_base)
			program[args[2]] = program[args[0]] * program[args[1]]
			p += 4
		elif opcode == 3: #Read
			while len(buffer) == 0:
				inp = stdin.readline()
				buffer += [int(i) for i in inp.split(" ")]
			args = getargs(program, p, modes, 1, relative_base)
			program[args[0]] = buffer[0]
			buffer = buffer[1:]
			p += 2
		elif opcode == 4: #Write
			args = getargs(program, p, modes, 1, relative_base)
			print(program[args[0]], file=stdout)
			p += 2
			if returnonwrite:
				return p, relative_base
		elif opcode == 5: #Jump-if-true
			args = getargs(program, p, modes, 2, relative_base)
			if not program[args[0]] == 0:
				p = program[args[1]]
			else:
				p += 3
		elif opcode == 6: #Jump-if-false
			args = getargs(program, p, modes, 2, relative_base)
			if program[args[0]] == 0:
				p = program[args[1]]
			else:
				p += 3
		elif opcode == 7: #Less than
			args = getargs(program, p, modes, 3, relative_base)
			program[args[2]] = 1 if program[args[0]] < program[args[1]] else 0
			p += 4
		elif opcode == 8: #Equals
			args = getargs(program, p, modes, 3, relative_base)
			program[args[2]] = 1 if program[args[0]] == program[args[1]] else 0
			p += 4
		elif opcode == 9:
			args = getargs(program, p, modes, 1, relative_base)
			relative_base += program[args[0]]
			p += 2
		elif opcode == 99: #Exit
			break
		else:
			raise RuntimeError(f"Invalid opcode: {opcode}")

x, y = 100, 100
dirx, diry = 0, -1
panels = np.zeros((200, 200), dtype=np.int32)
painted = np.zeros((200, 200), dtype=np.int32)

program += [0] * 1000

state = (0, 0)
while state is not None:
	stdin = io.StringIO(f"{panels[y,x]}")
	stdout = io.StringIO("")
	state = computer(program, None, None, stdin, stdout, True, state[0], state[1])
	if state is None:
		break
	state = computer(program, None, None, stdin, stdout, True, state[0], state[1])
	outp = [int(i) for i in stdout.getvalue().split("\n")[:-1]]
	panels[y,x] = outp[0]
	painted[y,x] = 1
	if outp[1] == 0:
		dirx, diry = diry, -dirx
	else:
		dirx, diry = -diry, dirx
	x += dirx
	y += diry

print(np.sum(painted))