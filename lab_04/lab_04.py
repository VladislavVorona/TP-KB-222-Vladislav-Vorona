import operator

class CalcRPN:
	def __init__(self):
		self.operators = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv, '^': operator.pow}

	def NumCheck(self, unit):
		return unit.isdigit()

	def OpPrior(self, operator):
		Prior = {'+': 0, '-': 0, '*': 1, '/': 1, '^': 2}
		return Prior.get(operator, -1)

	def RPNGenerator(self, UserInput):
		TempInfo = []
		RPNRes = []

		for xx in UserInput.split():
			if self.NumCheck(xx):
				RPNRes.append(xx)
			elif xx == '(':
				TempInfo.append(xx)
			elif xx == ')':
				while TempInfo and TempInfo[-1] != '(':
					RPNRes.append(TempInfo.pop())
				TempInfo.pop()
			elif xx in self.operators:
				while TempInfo and self.OpPrior(TempInfo[-1]) >= self.OpPrior(xx):
					RPNRes.append(TempInfo.pop())
				TempInfo.append(xx)

		while TempInfo:
			RPNRes.append(TempInfo.pop())

		return RPNRes

	def CalculateRPN(self, RPNText):
		TempInfo = []

		for xx in RPNText:
			if self.NumCheck(xx):
				TempInfo.append(float(xx))
			elif xx in self.operators:
				if len(TempInfo) < 2:
					raise ValueError("Не достатньо операндів для оператора {}".format(xx))
				xx2, xx1 = TempInfo.pop(), TempInfo.pop()
				result = self.operators[xx](xx1, xx2)
				TempInfo.append(result)


		if len(TempInfo) != 1:
			raise ValueError("Недійсний вираз")

		return TempInfo[0]

if __name__ == '__main__':
	CalcRPNClass = CalcRPN()

	UserInput = input("Введіть ваш приклад: ")
	print("Приклад користувача:", UserInput)

	RPNText = CalcRPNClass.RPNGenerator(UserInput)
	print("Зворотній польський запис:", ' '.join(RPNText))

	result = CalcRPNClass.CalculateRPN(RPNText)
	print("Відповідь:", result)
