from Student import Student

class StudentList:
	def __init__(self):
		self.students = []

	def addNewElement(self):
		name = input("Please enter student name: ")
		phone = input("Please enter student phone: ")

		while True:
			try:
				age = int(input("Please enter student age: "))
				break
			except ValueError:
				print("Wrong student age")

		email = input("Please enter student email: ")
		student = Student(name, phone, age, email)
		self.students.append(student)
		self.students.sort(key=lambda x: (x.name, x.age))
		print("New element has been added")

	def deleteElement(self, name):
		found = False
		for student in self.students:
			if name == student.name:
				found = True
				print(f"Student {name} found. Please update the information:")
				deletePosition = self.students.index(student)
				break

		if not found:
			print("Student not found")
			return

		del self.students[deletePosition]

	def updateElement(self, name):
		found = False
		for student in self.students:
			if name == student.name:
				found = True
				print(f"Student {name} found. Please update the information:")
				deletePosition = self.students.index(student)
				break

		if not found:
			print("Student not found")
			return

		del self.students[deletePosition]

		nname = input("Please enter new name: ")
		if nname == "":
			nname = student.name

		insertPosition = 0
		for item in self.students:
			if nname > item.name:
				insertPosition += 1
			else:
				break

		nstudent = Student(nname, student.phone, student.age, student.email)
		self.students.insert(insertPosition, nstudent)

		nphone = input("Please enter updated phone: ")
		if nphone != "":
			nstudent.phone = nphone
			
		while True:
			try:
				nage = input("Please enter updated age: ")
				if nage != "":
					nstudent.age = int(nage)
				break
			except ValueError:
				print("Wrong student age")

		nemail = input("Please enter updated email: ")
		if nemail != "":
			nstudent.email = nemail 

		print("Element has been updated")


	def printAllList(self):
		for student in self.students:
			str_for_print = f"Student name is {student.name}, Phone is {student.phone}, Age is {student.age}, Email is {student.email}"
			print(str_for_print)
		