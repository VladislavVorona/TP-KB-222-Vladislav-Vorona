import logging

logging.basicConfig(filename='logs/Task3.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(module)s - %(funcName)s - %(message)s - line %(lineno)d')

class student_class:
	def __init__(self, name, age):
		self.name = name
		self.age = age

def sort(startfile, lastfile, sortk):
	try:
		with open(startfile, 'r') as file:
			logging.info("Отримання даних")
			lines = [line.strip() for line in file]

		logging.info("Розбиття рядків на об'єкти класу")

		students = []

		for line in lines:
			studline = line.split()
			name = studline[0]
			age = int(studline[1])
			student = student_class(name=name, age=age)
			students.append(student)

		logging.info("Сортування")
		students_sort = sorted(students, key=lambda student: (sortk(student), student.age))

		with open(lastfile, 'w') as file:
			for student in students_sort:
				logging.info(f"Запис даних до файлу {lastfile}")
				file.write(f"{student.name} {student.age}\n")

		logging.info(f"Дані файлу {startfile} було відсортовано та збережено у {lastfile}")

		print(f"Відсортований список:\n")
		for student in students_sort:
			print(f"{student.name} {student.age}")

	except Exception as error:
		logging.error(f"Сталася помилка: {str(error)}")
		print(f"Сталася помилка: {str(error)}")

logging.info("Виклик першої функції сортування")
sort('Task3.txt', 'Task3_Name.txt', lambda student: student.name)

logging.info("Виклик другої функції сортування")
sort('Task3.txt', 'Task3_Age.txt', lambda student: student.age)
