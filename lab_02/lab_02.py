import csv
import sys

def FileLoad(file):
	with open(file, encoding="utf-8") as file:
		result = csv.DictReader(file)
		return [row for row in result]

def SaveFile(file, list):
	names = ["name", "phone", "age", "email"]
	try:
		with open(file, "w", newline="", encoding="utf-8") as file:
			ResFile = csv.DictWriter(file, fieldnames=names)
			ResFile.writeheader()
			ResFile.writerows(list)
		print(f"The data is saved in {file}.")
	except IOError as e:
		print(f"Error saving to {file}: {e}")

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
	found = False
	for student in list:
		if name == student["name"]:
			found = True
			print(f"Student {name} found. Please update the information:")

			nname = input("Please enter new name: ")
			deletePosition = list.index(student)
			break

	if not found:
		print("Student not found")
		return

	del list[deletePosition]

	insertPosition = deletePosition

	if nname != "":
		student["name"] = nname
		insertPosition = 0
		for item in list:
			if nname > item["name"]:
				insertPosition += 1
			else:
				break

	list.insert(insertPosition, student)

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

list = [ ]
AFile = None

def main():
	global AFile

	if len(sys.argv) > 1:
		try:
			file = sys.argv[1]
			list.extend(FileLoad(file))
			print("Data loaded successfully.")
			AFile = file
		except IOError as e:
			print("File upload error.")
	else:
		print("No CSV file specified in the command line arguments.")
			
	while True:
		print(f"Active CSV file: {AFile}")
		choice = input("Please specify the action [ C create, U update, D delete, P print, L load, S save, X exit ] ")
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
			case "L":
				try:
					file = input("Enter the name of the CSV file from which you want to download data: ")
					list.extend(FileLoad(file))
					print("Data loaded successfully.")
					AFile = file
				except IOError as e:
					print("File upload error.")
			case "S":
				file = input("Enter a name for the CSV file to save the data to: ")
				SaveFile(file, list)
			case "X":
				print("Exit")
				break
			case _:
				print("Wrong choice")

if __name__ == "__main__":
	main()