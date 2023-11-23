import csv
from Student import Student

class FileHandler:
	@staticmethod
	def LoadFile(file, StudentListClass):
		StudentListClass.students = []
		with open(file, encoding="utf-8") as file:
			result = csv.DictReader(file)
			StudentListClass.students.extend([Student(row["name"], row["phone"], row["age"], row["email"]) for row in result])
		return StudentListClass

	@staticmethod
	def SaveFile(file, StudentListClass):
		names = ["name", "phone", "age", "email"]
		try:
			with open(file, "w", newline="", encoding="utf-8") as file:
				ResFile = csv.DictWriter(file, fieldnames=names)
				ResFile.writeheader()
				ResFile.writerows([vars(student) for student in StudentListClass.students])
			print(f"The data is saved in {file.name}.")
		except IOError as e:
			print(f"Error saving to {file}: {e}")