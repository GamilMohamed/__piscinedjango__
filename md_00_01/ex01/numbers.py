import sys

def readfile():
	try:
		with open("numbers.txt", 'r') as file:
			line = file.readline().split(",")
			for number in line:
				print(f"num: {number}")
	except FileNotFoundError:
		print("File not found")
		return

if __name__ == "__main__":
	readfile()