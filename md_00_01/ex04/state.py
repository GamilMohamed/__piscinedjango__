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

import sys

def ok(where, inside) :
	for i in where:
		if where[i] == inside:
			return (i)
	return None; 


def find_state(city):
	short = ok(capital_cities, city)
	state = ok(states, short)
	if state == None:
		return ("Unknown capital city")
	return state

if __name__ == "__main__":
	if len(sys.argv) == 2:
		print(find_state(sys.argv[1]))