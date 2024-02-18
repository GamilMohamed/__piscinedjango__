import sys

def delete_space(s):
	s = s.split(',')
	for x in range(len(s) - 1, -1, -1):
		s[x] = s[x].strip()
		if s[x].isspace() or len(s[x]) == 0:
			s.pop(x)
	return s

def find_state_by_abbreviation(states, abb) :
	for state, abbr in states.items():
		if abbr == abb:
			return (state)
	return None; 

def find_city_by_state(capital_cities, state):
	for k, v in capital_cities.items():
		if k == state:
			return v
	return None

def find_abbreviation_by_capital(capital_cities, city):
	for k, v in capital_cities.items():
		if v == city:
			return k
	return None

def all_in(s):
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


	if ",," in s:
		return

	states_upper = {key.upper(): value.upper() for key, value in states.items()}
	capital_cities_upper = {key.upper(): value.upper() for key, value in capital_cities.items()}

	s = delete_space(s)
	s_upper = [x.upper() for x in s]
	for x in range(len(s_upper)):
		if s_upper[x] in states_upper:
			abb = states_upper[s_upper[x]]
		elif s_upper[x] in capital_cities_upper.values():
			abb = find_abbreviation_by_capital(capital_cities_upper, s_upper[x])
		else:
			print(f"{s[x]} is neither a capital city nor a state")
			continue
		get_city = find_city_by_state(capital_cities, abb)
		get_state = find_state_by_abbreviation(states, abb)
		print(f"{get_city} is the capital of {get_state}")

if __name__ == "__main__":
	if len(sys.argv) == 2:
		all_in(sys.argv[1])