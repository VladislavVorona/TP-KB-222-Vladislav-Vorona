class soft:
	def __init__(self, name, year, dev):
		self.name = name
		self.year = year
		self.dev = dev

	def __str__(self):
		print("Задіяно метод класcу __str__")
		return f"{self.name} була розроблена {self.dev} у {self.year} році"

	def __eq__(self, other):
		print("Задіяно метод класcу __eq__")
		return self.year == other.year

	def __ne__(self, other):
		print("Задіяно метод класcу __ne__")
		return self.year != other.year

	def __lt__(self, other):
		print("Задіяно метод класcу __lt__")
		return self.year < other.year

	def __gt__(self, other):
		print("Задіяно метод класcу __gt__")
		return self.year > other.year

	def __le__(self, other):
		print("Задіяно метод класcу __le__")
		return self.year <= other.year

	def __ge__(self, other):
		print("Задіяно метод класcу __ge__")
		return self.year >= other.year

soft1 = soft("Sublime Text", 2008, "Sublime HQ")
soft2 = soft("Visual Studio Code", 2015, "Microsoft")

print(soft1)

print(soft1 == soft2)
print(soft1 != soft2)
print(soft1 < soft2)
print(soft1 > soft2)

#-------------------------------------------------------------

playlist = ["Be my guest - Azari", "МОЯ КРАЇНА - YARMAK", "The wolf - SIAMÉS"]

class playlist_class:
	def __init__(self, songs):
		self.songs = songs

	def __len__(self):
		print("Задіяно метод класcу __len__")
		return len(self.songs)

answer = playlist_class(playlist)
print(len(answer))

#-------------------------------------------------------------

class playlist_class:
	def __init__(self, songs):
		self.songs = songs

	def __getitem__(self, index):
		print("Задіяно метод класcу __getitem__")
		return self.songs[index]

answer = playlist_class(playlist)
print(answer[1])

#-------------------------------------------------------------

class playlist_class:
	def __init__(self, songs):
		self.songs = songs

	def __setitem__(self, index, value):
		print("Задіяно метод класcу __setitem__")
		self.songs[index] = value

answer = playlist_class(playlist)
answer[2] = "Kaibutsu - LiSA"
print(answer.songs)

#-------------------------------------------------------------

class playlist_class:
	def __init__(self, songs):
		self.songs = songs

	def __delitem__(self, index):
		print("Задіяно метод класcу __delitem__")
		del self.songs[index]

answer = playlist_class(playlist)
del answer[2]
print(answer.songs)

#-------------------------------------------------------------

class playlist_class:
	def __init__(self, songs):
		self.songs = songs

	def __contains__(self, item):
		print("Задіяно метод класcу __contains__")
		return item in self.songs

answer = playlist_class(playlist)
print("МОЯ КРАЇНА - YARMAK" in answer)
print("Be my guest - Azari" in answer)

#-------------------------------------------------------------

class minicalc_class:
	def __call__(self, x, y):
		print("Задіяно метод класcу __call__")
		return x + y

minicalc = minicalc_class()
answer = minicalc(5, 5)
print(answer)

#-------------------------------------------------------------

class soft:
	def __init__(self, name, year, developer):
		self.name = name
		self.year = year
		self.developer = developer

	def __getattr__(self, name):
		print("Задіяно метод класcу __getattr__")
		return f"Атрибуту {name} не існує"

	def __setattr__(self, name, value):
		print("Задіяно метод класcу __setattr__")
		print(f"Внесення {value} в {name}")
		super().__setattr__(name, value)

answer = soft("Visual Studio Code", 2015, "Microsoft")
print(answer.version)