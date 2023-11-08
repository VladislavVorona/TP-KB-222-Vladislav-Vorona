list = [
	{"name": "Bob", "phone": "0631234567", "age": 20, "email": "bob@example.com"},
	{"name": "Emma", "phone": "0631234567", "age": 22, "email": "emma@example.com"},
	{"name": "Jon", "phone": "0631234567", "age": 21, "email": "jon@example.com"},
	{"name": "Zak", "phone": "0631234567", "age": 23, "email": "zak@example.com"}
]


def printAllList():
	for elem in list:
		strForPrint = f"Student name is {elem['name']}, Phone is {elem['phone']}, Age is {elem['age']}, Email is {elem['email']}"
		print(strForPrint)
	return


def addNewElement():
	name = input("Please enter student name: ")
	phone = input("Please enter student phone: ")

	while True:
		try:
			age = int(input("Please enter student age: "))
			break
		except ValueError:
			print("Wrong student age")

	email = input("Please enter student email: ")
	
	newItem = {"name": name, "phone": phone, "age": age, "email": email}
	insertPosition = 0
	for item in list:
		if name > item["name"]:
			insertPosition += 1
		else:
			break
	list.insert(insertPosition, newItem)
	print("New element has been added")
	return

def deleteElement():
	name = input("Please enter name to be deleted: ")
	deletePosition = -1
	for item in list:
		if name == item["name"]:
			deletePosition = list.index(item)
			break
	if deletePosition == -1:
		print("Element was not found")
	else:
		print("Del position " + str(deletePosition))
		del list[deletePosition]
	return

def updateElement():
	name = input("Please enter name to be updated: ")
	for student in list:
		if name == student["name"]:
			print(f"Student {name} found. Please update the information:")

			nname = input("Please enter new name: ")
			if nname != "":
				student["name"] = nname
				list.sort(key=lambda x: x["name"])

			phone = input("Please enter updated phone: ")
			if phone != "":
				student["phone"] = phone

			while True:
				try:
					age = input("Please enter updated age: ")
					if age != "":
						student["age"] = int(age)
					break
				except ValueError:
					print("Wrong student age")

			email = input("Please enter updated email: ")
			if email != "":
				student["email"] = email	

			print("Element has been updated")
			return
	print("Student not found")


def main():
	while True:
		choice = input("Please specify the action [ C create, U update, D delete, P print,  X exit ] ")
		match choice.upper():
			case "C":
				print("New element will be created:")
				addNewElement()
				printAllList()
			case "U":
				print("Existing element will be updated")
				updateElement()
				printAllList()
			case "D":
				print("Element will be deleted")
				deleteElement()
				printAllList()
			case "P":
				print("List will be printed")
				printAllList()
			case "X":
				print("Exit")
				break
			case _:
				print("Wrong choice")

main()
