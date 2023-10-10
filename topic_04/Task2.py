def getxx():
	while True:
		vir = input('Введіть вираз через пробіли або "q", щоб вийти, наприклад, 5 + 5: ')

		if vir.lower() == "q":
			print("Вихід")
			break
		else:
			xx = vir.split()

			try:
				xx1 = float(xx[0])
				op = xx[1]
				xx2 = float(xx[2])
				return xx1, op, xx2

			except ValueError:
				print("Було введено невірні числові значення")
				continue
				
			except IndexError:
				print("Було введено недостатню кількість значень")
				continue

while True:
	xx1, op, xx2 = getxx()

	def plus(xx1, xx2):
		return xx1 + xx2

	def minus(xx1, xx2):
		return xx1 - xx2

	def mno(xx1, xx2):
		return xx1 * xx2

	def dil(xx1, xx2):
		return xx1 / xx2

	try:
		if op == "+":
			res = plus(xx1, xx2)
		elif op == "-":
			res = minus(xx1, xx2)
		elif op == "*":
			res = mno(xx1, xx2)
		elif op == "/":
			res = dil(xx1, xx2)
		else:
			print("Помилка розпізнавання операції")
			continue

	except ZeroDivisionError:
		print("Ділення на нуль")
		continue

	print(f"Відповідь: {res}")
