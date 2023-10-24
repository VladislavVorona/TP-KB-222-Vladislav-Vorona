import logging
import os

logging.basicConfig(filename='logs/Task2.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(module)s - %(funcName)s - %(message)s - line %(lineno)d')

def sort(startfile, lastfile, sortk):
    try:
        with open(startfile, 'r') as file:
            logging.info("Отримання даних")
            lines = [line.strip() for line in file]

        logging.info("Розбиття рядків на словники")
        students = [{'name': line.split()[0], 'grade': int(line.split()[1])} for line in lines]

        logging.info("Сортування")
        students_sort = sorted(students, key=lambda student: (sortk(student), student['grade']))

        with open(lastfile, 'w') as file:
            for student in students_sort:
                logging.info(f"Запис даних до файлу {lastfile}")
                file.write(f"{student['name']} {student['grade']}\n")

        logging.info(f"Дані файлу {startfile} було відсортовано та збережено у {lastfile}")

        print(f"Відсортований список:\n")

        for student in students_sort:
            print(f"{student['name']} {student['grade']}")

    except Exception as error:
        logging.error(f"Сталася помилка: {str(error)}")
        print(f"Сталася помилка: {str(error)}")

logging.info("Виклик першої функції сортування")
sort('Task2.txt', 'Task2_Name.txt', lambda student: student['name'])

logging.info("Виклик другої функції сортування")
sort('Task2.txt', 'Task2_Grade.txt', lambda student: student['grade'])
