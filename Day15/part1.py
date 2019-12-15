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

field = np.array([" "] * 1764).reshape((42, 42))
sx, sy = 21, 21
dx, dy = 21, 21
field[sy,sx] = "."
dx2, dy2 = 0, -1

def draw(field, dx, dy, sx, sy, drawdrone=True):
	print("=" * 44)
	for y in range(42):
		print("|", end="")
		for x in range(42):
			if drawdrone and x == dx and y == dy:
				print("D", end="")
			elif x == sx and y == sy:
				print("S", end="")
			else:
				print(field[y,x], end="")
		print("|")
	print("=" * 44)

def getd(inp):
	if inp == "1":
		return 0, -1
	elif inp == "2":
		return 0, 1
	elif inp == "3":
		return -1, 0
	elif inp == "4":
		return 1, 0

def invgetd(dx, dy):
	if dx == 0 and dy == -1:
		return "1"
	elif dx == 0 and dy == 1:
		return "2"
	elif dx == -1 and dy == 0:
		return "3"
	elif dx == 1 and dy == 0:
		return "4"

trace = [(sx, sy)]
state = (0, 0)
while True:
	draw(field, dx, dy, sx, sy)
	stdout = io.StringIO("")
	if field[dy-dx2,dx+dy2] == " ":
		inp = invgetd(dy2, -dx2)
	elif field[dy+dx2,dx-dy2] == " ":
		inp = invgetd(-dy2, dx2)
	elif field[dy-dy2,dx-dx2] == " ":
		inp = invgetd(-dx2, -dy2)
	elif field[dy+dy2,dx+dx2] == " ":
		inp = invgetd(dx2, dy2)
	elif len(trace) > 1:
		inp = invgetd(trace[-2][0] - trace[-1][0], trace[-2][1] - trace[-1][1])
	else:
		inp = ""
		while len(inp) == 0:
			inp = input()
		inp = inp[0]
	stdin = io.StringIO("1" if inp == "w" else "2" if inp == "s" else "3" if inp == "a" else "4" if inp == "d" else inp)
	state = computer(program, stdout=stdout, stdin=stdin, returnonwrite=True, state=state[0], base_state=state[1])
	dx2, dy2 = getd(stdin.getvalue())
	if stdout.getvalue() == "0\n":
		field[dy+dy2,dx+dx2] = "#"
	elif stdout.getvalue() == "1\n":
		dx += dx2
		dy += dy2
		field[dy,dx] = "."
		if len(trace) > 1 and trace[-2][0] == dx and trace[-2][1] == dy:
			trace = trace[:-1]
		else:
			trace.append((dx, dy))
	elif stdout.getvalue() == "2\n":
		dx += dx2
		dy += dy2
		field[dy,dx] = "O"
		if len(trace) > 1 and trace[-2][0] == dx and trace[-2][1] == dy:
			trace = trace[:-1]
		else:
			trace.append((dx, dy))
		draw(field, dx, dy, sx, sy, False)
		print(len(trace)-1)
		break
	sys.stdout.flush()
	if state is None:
		break