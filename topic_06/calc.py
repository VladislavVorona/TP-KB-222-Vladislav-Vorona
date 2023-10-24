import logging
from functions import *
from operations import getxx

logging.basicConfig(filename='logs/calc.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(module)s - %(funcName)s - %(message)s - line %(lineno)d')

while True:
	logging.info(f"Запит змінних у користувача")
	try:
		xx1, op, xx2 = getxx()
	except TypeError:
		logging.info(f"Закінчення виконання роботи за допомогою 'q'")
		break

	try:
		logging.info(f"Перевірка операції: {op}")
		if op == "+":
			logging.info(f"Перевірка функції: {op}")
			res = plus(xx1, xx2)
		elif op == "-":
			logging.info(f"Перевірка функції: {op}")
			res = minus(xx1, xx2)
		elif op == "*":
			logging.info(f"Перевірка функції: {op}")
			res = mno(xx1, xx2)
		elif op == "/":
			logging.info(f"Перевірка функції: {op}")
			res = dil(xx1, xx2)
		else:
			logging.error("Помилка розпізнавання операції")
			print("Помилка розпізнавання операції")
			continue
		logging.info(f"Виконано операцію: {xx1} {op} {xx2} = {res}")
		print(f"Відповідь: {res}")

	except ZeroDivisionError:
		logging.error("Ділення на нуль")
		print("Ділення на нуль")
		continue

	except Exception as e:
		logging.error(f"Сталася помилка: {str(e)}")
		print(f"Сталася помилка: {str(e)}")