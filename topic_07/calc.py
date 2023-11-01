import logging
from functions import functions_class

logging.basicConfig(filename='logs/calc.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(module)s - %(funcName)s - %(message)s - line %(lineno)d')

while True:
	logging.info("Запит змінних у користувача")
	try:
		calc = functions_class(*functions_class.getxx())
	except TypeError:
		logging.info("Закінчення виконання роботи за допомогою 'q'")
		break

	try:
		logging.info(f"Перевірка операції: {calc.op}")
		res = calc.operations()
		logging.info(f"Виконано операцію: {calc.xx1} {calc.op} {calc.xx2} = {res}")
		print(f"Відповідь: {res}")

	except ZeroDivisionError:
		logging.error("Ділення на нуль")
		print("Ділення на нуль")
		continue

	except Exception as e:
		logging.error(f"Сталася помилка: {str(e)}")
		print(f"Сталася помилка: {str(e)}")
