import copy
import numpy as np
import sympy.utilities.iterables as sui
import io
import sys

with open("Input.txt", "r") as f:
	line = f.readline().split(",")
	program = [int(i) for i in line]

def getargs(program, p, modes, argc):
	args = []
	for i in range(argc):
		args.append(p+i+1 if len(modes) >= i + 1 and modes[i] == 1 else program[p+i+1])
	return args

def computer(program, noun=None, verb=None, stdin=sys.stdin, stdout=sys.stdout, returnonwrite=False, state=0):
	if not noun is None:
		program[1] = noun
	if not verb is None:
		program[2] = verb
	p = state
	buffer = []
	while True:
		opcode = int(str(program[p])[-min(2, len(str(program[p]))):])
		if len(str(program[p])) > 2:
			modepart = str(program[p])[:len(str(program[p]))-2][::-1]
			modes = [int(modepart[i]) for i in range(len(modepart))]
		else:
			modes = []
		if opcode == 1: #Add
			args = getargs(program, p, modes, 3)
			program[args[2]] = program[args[0]] + program[args[1]]
			p += 4
		elif opcode == 2: #Mult
			args = getargs(program, p, modes, 3)
			program[args[2]] = program[args[0]] * program[args[1]]
			p += 4
		elif opcode == 3: #Read
			while len(buffer) == 0:
				inp = stdin.readline()
				buffer += [int(i) for i in inp.split(" ")]
			args = getargs(program, p, modes, 1)
			program[args[0]] = buffer[0]
			buffer = buffer[1:]
			p += 2
		elif opcode == 4: #Write
			args = getargs(program, p, modes, 1)
			stdout.write(f"{program[args[0]]}\n")
			p += 2
			if returnonwrite:
				return p
		elif opcode == 5: #Jump-if-true
			args = getargs(program, p, modes, 2)
			if not program[args[0]] == 0:
				p = program[args[1]]
			else:
				p += 3
		elif opcode == 6: #Jump-if-false
			args = getargs(program, p, modes, 2)
			if program[args[0]] == 0:
				p = program[args[1]]
			else:
				p += 3
		elif opcode == 7: #Less than
			args = getargs(program, p, modes, 3)
			program[args[2]] = 1 if program[args[0]] < program[args[1]] else 0
			p += 4
		elif opcode == 8: #Equals
			args = getargs(program, p, modes, 3)
			program[args[2]] = 1 if program[args[0]] == program[args[1]] else 0
			p += 4
		elif opcode == 99: #Exit
			break
		else:
			raise RuntimeError(f"Invalid opcode: {opcode}")

def calcthrust(program, p):
	outp = 0
	states = [0, 0, 0, 0, 0]
	amplifiers = [copy.copy(program), copy.copy(program), copy.copy(program), copy.copy(program), copy.copy(program)]
	for i in range(len(p)):
		stdin = io.StringIO(f"{p[i]} {outp}")
		stdout = io.StringIO("")
		states[i] = computer(amplifiers[i], stdin=stdin, stdout=stdout, returnonwrite=True)
		outp = int(stdout.getvalue())
	while not None in states:
		for i in range(len(p)):
			stdin = io.StringIO(f"{outp}\n")
			stdout = io.StringIO("")
			states[i] = computer(amplifiers[i], stdin=stdin, stdout=stdout, state=states[i], returnonwrite=True)
			if None in states:
				break
			outp = int(stdout.getvalue())
	return outp

maxval = 0
for p in sui.multiset_permutations(np.array([5, 6, 7, 8, 9])):
	maxval = max(maxval, calcthrust(program, p))
print(maxval)