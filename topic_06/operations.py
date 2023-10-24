import logging

def getxx():
	while True:
		vir = input('Введіть вираз через пробіли або "q", щоб вийти, наприклад, 5 + 5: ')
		logging.info(f'Користувач ввів: {vir}')

		if vir.lower() == "q":
			print("Вихід")
			logging.info("Користувач вийшов з програми")
			break
		else:
			xx = vir.split()

			try:
				xx1 = float(xx[0])
				logging.info(f'Форматовано значення: xx1 = {xx1}')
				op = xx[1]
				logging.info(f'Отримано значення: op = {op}')
				xx2 = float(xx[2])
				logging.info(f'Форматовано значення: xx2 = {xx2}')
				logging.info(f'Отримано значення: xx1 = {xx1}, op = {op}, xx2 = {xx2}')
				return xx1, op, xx2

			except ValueError:
				print("Було введено невірні числові значення")
				logging.error("Було введено невірні числові значення")

			except IndexError:
				print("Було введено недостатню кількість значень")
				logging.error("Було введено недостатню кількість значень")
