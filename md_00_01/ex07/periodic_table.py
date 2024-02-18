from tkinter import Menu
from turtle import position


def periodic_table():
	mendeleev = {}
	with open("periodic_table.txt", "r") as file:
		elements = file.read().split("\n")
		for e in elements:
			val = e.split(",")
			if len(val) != 5:
				continue
			temp = {}
			typenpos = [x.strip() for x in val[0].split("=")]
			val = [x.strip() for x in val]
			temp["name"] = typenpos[0]
			temp["pos"] = typenpos[1].split(":")[1]
			temp["id"] = val[1].split(":")[1]
			temp["small"] = val[2].split(":")[1].strip()
			temp["molar"] = val[3].split(":")[1]
			temp["electron"] = list(val[4].split(":")[1].split(" "))
			mendeleev[typenpos[0]] = temp
			# print(mendeleev[typenpos[0]])
	create_file(mendeleev)

def create_file(tab):
	with open("periodic_table.html", "w") as file:
		file.write('<!DOCTYPE html>\n<html lang="en">\n<head>\n\t<meta charset="UTF-8">\n\t<meta name="viewport" content="width=device-width, initial-scale=1.0">\n\t<title>Periodic table</title>\n</head>\n<body>\n\t')
		file.write('<table>\n')
		for x in tab:
			file.write(f'\t<tr>\n\t\t\t<h4>{tab[x]["name"]}</h4>\n\t\t\t<ul>\n\t\t\t\t<li>Pos:{tab[x]["pos"]}</li>\n\t\t\t\t<li>ID:{tab[x]["id"]}</li>\n\t\t\t\t<li>Small:{tab[x]["small"]}</li>\n\t\t\t\t<li>Molar:{tab[x]["molar"]}</li>\n\t\t\t\t<li>Electron:{tab[x]["electron"]}</li>\n\t\t\t</ul>\n\t\t</tr>')
			# file.write(f'\n\t\t<tr>\n\t\t\t<h4>	{tab[x]["name"]}</h4>\n\t\t\t<ul>\n\t\t\t\t<li>{tab[x]["pos"]}</li>\n\t\t\t\t<li>{tab[x]["id"]}</li>\n\t\t\t\t<li>{tab[x]["small"]}</li>\n\t\t\t\t<li>{tab[x]["molar"]}</li>\n\t\t\t\t<li>{tab[x]["electron"]}</li>\n\t\t\t</ul>\n\t\t</tr>\n\t')
			# file.write(f'\n\t<div style="left: {tab[x]["pos"]}; top: {tab[x]["pos"]};">\n\t\t<h1>{tab[x]["name"]}</h1>\n\t\t<p>Id: {tab[x]["id"]}</p>\n\t\t<p>Small: {tab[x]["small"]}</p>\n\t\t<p>Molar: {tab[x]["molar"]}</p>\n\t\t<p>Electron: {tab[x]["electron"]}</p>\n\t</div>')

		file.write('</table>\n')
		file.write('\n</body>\n</html>\n\n')

if __name__ == "__main__":
	periodic_table()