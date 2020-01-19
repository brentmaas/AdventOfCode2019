import copy

actions = []
with open("Input.txt", "r") as f:
	line = f.readline()
	while line:
		actions.append(line.replace("\n", ""))
		line = f.readline()

num_cards = 10007
cards = [i for i in range(num_cards)]

for a in actions:
	if a == "deal into new stack":
		cards = cards[::-1]
	elif a.startswith("cut "):
		N = int(a.split(" ")[-1])
		cards = cards[N:] + cards[:N]
	elif a.startswith("deal with increment "):
		N = int(a.split(" ")[-1])
		tmpcards = copy.copy(cards)
		for i in range(len(cards)):
			cards[(N * i) % num_cards] = tmpcards[i]
	else:
		raise RuntimeError(f"Invalid action: {a}")

print(cards.index(2019))