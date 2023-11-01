import logging

class functions_class:
	def __init__(self, xx1, op, xx2):
		self.xx1 = xx1
		self.op = op
		self.xx2 = xx2


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
					if len(xx) != 3:
						raise ValueError("Було введено недостатню кількість значень")

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

	def operations(self):
		if self.op == "+":
			return self.plus(self.xx1, self.xx2)
		elif self.op == "-":
			return self.minus(self.xx1, self.xx2)
		elif self.op == "*":
			return self.mno(self.xx1, self.xx2)
		elif self.op == "/":
			return self.dil(self.xx1, self.xx2)
		else:
			raise ValueError("Помилка розпізнавання операції")

	@staticmethod
	def plus(xx1, xx2):
		return xx1 + xx2

	@staticmethod
	def minus(xx1, xx2):
		return xx1 - xx2

	@staticmethod
	def mno(xx1, xx2):
		return xx1 * xx2

	@staticmethod
	def dil(xx1, xx2):
		if xx2 == 0:
			raise ZeroDivisionError("Ділення на нуль")
		return xx1 / xx2
