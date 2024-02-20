#!/usr/bin/python3

def mendeleev_tab():
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
	return mendeleev
    

def writecssfile():
    f = open("periodic_table.css", "w")
    f.write("""      table {
        border-collapse: collapse;
      }
      h4 {
        text-align: center;
      }
      ul {
        list-style: none;
        padding-left: 0px;
      }
      td {
        border: 1px solid black;
        padding: 10px;
        width: 100px;
      }
      .none {
        border: none;
      }
""")
    f.close()

def print_bloc(element):
    str = """      <td>
       <h4>{}</h4>
        <ul>
          <li>No: {}</li>
          <li>Symbol: {}</li>
          <li>molar: {}</li>  
          <li>{} electron</li>  
        </ul>
      </td>\n"""
    return str.format(element["name"], element["id"], element["small"], element["molar"], element["electron"])

def main():
    HEADER = """<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <title>periodic_table</title>
    <link rel="stylesheet" href="periodic_table.css">
  </head>
  <body>
  <table>
  """
    FOOTER = """  </table>
  </body>
</html>
"""
    EMPTY = "      <td class='none'></td>\n"
    periodic_table = mendeleev_tab()
    f = open("periodic_table.html", "w")
    f.write(HEADER)
    actpos = 0
    for x in periodic_table:
      val = int(periodic_table[x]["pos"]) # 0
      while (actpos < val):
        f.write(EMPTY)
        actpos += 1
      if (val == 0):
        f.write("  <tr>\n")
      f.write(print_bloc(periodic_table[x]))
      actpos += 1
      if (val == 17):
        actpos = 0
        f.write("  </tr>\n")
    f.write(FOOTER)
    writecssfile()

if __name__ == '__main__':
    main()
