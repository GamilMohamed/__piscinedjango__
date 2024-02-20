def readfile():
	with open("numbers.txt", 'r') as file:
		line = file.readline().split(",")
		for number in line:
			print(f"num: {number}")

if __name__ == "__main__":
	readfile()