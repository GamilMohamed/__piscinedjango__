def my_var():
	var = 42
	print(f"{var} is of type {type(var)}")
	var = "42"
	print(f"{var} is of type {type(var)}")
	var = "quarante-deux"
	print(f"{var} is of type {type(var)}")
	var = 42.0
	print(f"{var} is of type {type(var)}")
	var = True
	print(f"{var} is of type {type(var)}")
	var = [42]
	print(f"{var} is of type {type(var)}")
	var = {42: 42}
	print(f"{var} is of type {type(var)}")
	var = (42,)
	print(f"{var} is of type {type(var)}")
	var = set()
	print(f"{var} is of type {type(var)}")

if __name__ == '__main__':
	my_var()