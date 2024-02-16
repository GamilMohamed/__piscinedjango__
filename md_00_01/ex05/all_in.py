import sys

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

def all_in(s):
	print(f"len de s {len(s)}")
	strlen = len(s)
	for c in range(0, strlen):
		if c < strlen - 1 and s[c] == ',' and s[c + 1] == ',': 
			print(f"c vaut {c} s[c] vaut {s[c]}")# i vaut {i}")
	s = s.split(',')
	citynstate = {capital_cities[i] for i in capital_cities}
	citynstate.update({state for state in states})
	print(citynstate)

if __name__ == "__main__":
	if len(sys.argv) == 2:
		all_in(sys.argv[1])