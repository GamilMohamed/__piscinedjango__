import sys

def	replace(file):
	try:
		data = {}
		f = open("settings.py", "r")
		if not f:
			raise FileNotFoundError
		for line in f.readlines():
			print(f"Line: {line}")
			name = line.split("=")
			if len(name) != 2:
				raise ValueError(f"Error: invalid line in settings.py: {line}")
			data[name[0].strip()] = name[1].strip().replace("\"", "")
		f.close()
	except Exception as e:
		print(f"Error: {e}")
		return

	print(f"Data:\n{data}")
	try:
		with open(file, "r") as f:
			template = f.read()
			print(f"Template:\n{template}")
		with open(file.replace(".template", ".html"), "w") as f:
			for key in data:
				print(f"Replacing {key} with {data[key]}")
				template = template.replace(f"{{{key}}}", data[key])
				print(f"Template:\n{template}")
			f.write(template)
	except FileNotFoundError:
		print(f"Error: {file} not found")
if __name__ == "__main__":
	if len(sys.argv) == 2 and sys.argv[1].endswith(".template"):
		replace(sys.argv[1])
	else:
		print("Usage: python render.py <file.template>")