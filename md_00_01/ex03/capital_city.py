
import sys

def find_capital_city(state):
	states = {
	"Oregon" : "OR",
	"Alabama" : "AL",
	"New Jersey": "NJ",
	"Colorado" : "CO"
	}

	capital_cities = {
	"OR": "Salem",
	"AL": "Montgomery",
	"NJ": "Trenton",
	"CO": "Denver"
	}
	state = state.split()
	for i in range(len(state)):
		state[i] = state[i].capitalize()
	state = " ".join(state)
	print(state)
	if state in states:
		return capital_cities[states[state]]
	return "Unknown"


if __name__ == "__main__":
	if len(sys.argv) == 2:
		print(find_capital_city(sys.argv[1]))
