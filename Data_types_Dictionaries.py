People = {"nation": "Baganda", "colour": "Black", "Eyes": "Blue"}
People["country"] = "USA", "Chile"
People["Climate"] = ["Spring", "Summer"]
People["Climate"].append("Cloudy")
People["Birthday"] = 1955
People.get("age","invalid property")
go = People.get("nation","Invalid property")
key = "nation"

print(People)
print(People[key])
