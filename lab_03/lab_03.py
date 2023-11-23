import sys
from FileHandler import FileHandler
from StudentList import StudentList
from Student import Student

def main():
	AFile = None
	StudentListClass = StudentList()
	FileHandlerClass = FileHandler()

	if len(sys.argv) > 1:
		try:
			file = sys.argv[1]
			FileHandlerClass.LoadFile(file, StudentListClass)
			AFile = file
			print("Data loaded successfully.")
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
				StudentListClass.addNewElement()
				StudentListClass.printAllList()

			case "U":
				print("Existing element will be updated")
				name = input("Please enter name to be updated: ")
				StudentListClass.updateElement(name)
				StudentListClass.printAllList()

			case "D":
				print("Element will be deleted")
				name = input("Please enter name to be deleted: ")
				StudentListClass.deleteElement(name)
				StudentListClass.printAllList()

			case "P":
				print("List will be printed")
				StudentListClass.printAllList()

			case "L":
				try:
					file = input("Enter the name of the CSV file from which you want to download data: ")
					FileHandlerClass.LoadFile(file, StudentListClass)
					AFile = file
					print("Data loaded successfully.")
				except IOError as e:
					print("File upload error.")

			case "S":
				file = input("Enter a name for the CSV file to save the data to: ")
				FileHandlerClass.SaveFile(file, StudentListClass)
		
			case "X":
				print("Exit")
				break

			case _:
				print("Wrong choice")

if __name__ == "__main__":
	main()
