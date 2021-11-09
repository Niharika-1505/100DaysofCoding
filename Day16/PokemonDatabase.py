from prettytable import PrettyTable

table = PrettyTable()
table.add_column("ID", ["001", "002", "003", "004", "005"])
table.add_column("Pokemon Name", ["Chespin", "Quilladin", "Chesnaught", "Fennekin", "Braixen"])
table.add_column("Power Type", ["Grass", "Grass", "Grass . Fighting", "Fire", "Fire"])
table.align = "l"
print(table)
