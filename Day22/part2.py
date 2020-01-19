actions = []
with open("Input.txt", "r") as f:
	line = f.readline()
	while line:
		actions.append(line.replace("\n", ""))
		line = f.readline()

num_cards = 10007
needed_card = 1538
shuffles = 1

#num_cards = 119315717514047
#needed_card = 2020
#shuffles = 101741582076661

start = needed_card

a, b = 1, 0

for action in actions:
	if action.startswith("deal i"):
		a *= -1
		b = -b - 1
	elif action.startswith("c"):
		b -= int(action.split(" ")[-1])
	elif action.startswith("deal w"):
		N = int(action.split(" ")[-1])
		a *= N
		b *= N
	else:
		raise RuntimeError(f"Invalid action: {action}")

a %= num_cards
b %= num_cards

print(a, b, (a * start + b) % num_cards)

#(a(a(a(...a(ax+b)+b)+b)+b)...+b)+b) mod n = c
#(a^N x + a^(N-1)b + a^(N-2)b + ... + ab + b) mod n = c
#((a^N x) mod n + (a^(N-1)b) mod n + ... + (ab) mod n + b mod n) mod n = c