import random

def winner(gamerxx, computerxx):
	if gamerxx == computerxx:
		return "Нічія!"
	elif (gamerxx == "камінь" and computerxx == "ножиці") or \
		 (gamerxx == "ножиці" and computerxx == "папір") or \
		 (gamerxx == "папір" and computerxx == "камінь"):
		return "Ваша перемога!"
	else:
		return "Перемога комп'ютера!"

def computerfync(difficulty, gamerxx):
	xx = ["камінь", "ножиці", "папір"]
	
	if difficulty == "нормально":
		return random.choice(xx)
	elif difficulty == "складно":
		if gamerxx == "камінь":
			xx.append("папір")
			return random.choice(xx)
		elif gamerxx == "ножиці":
			xx.append("камінь")
			return random.choice(xx)
		else:
			xx.append("ножиці")
			return random.choice(xx)


while True:
	xx = ["камінь", "ножиці", "папір"]
	playerwin = 0
	computerwin = 0

	while True:
		try:
			rounds = int(input("Введіть кількість раундів: "))
			if rounds > 0:
				print(f"Було встановлено {rounds} раундів")
				break
			else:
				print("Було введено замалу кількість раундів")
		except ValueError:
			print("Було введено невірну кількість раундів")
	
	while True:		
		difficulty = input("Виберіть складність(нормально/складно): ")
		difficulty = difficulty.lower()
		if difficulty == "нормально" or difficulty == "складно":
			print(f"Було встановлено складність: {difficulty}")
			break
		else:
			difficulty = "нормально"
			print(f"Було встановлено складність: {difficulty}")
			break

	nowround = 0

	while nowround < rounds:
		gamerxx = input("Виберіть ваш жест(камінь, ножиці, папір): ")
		gamerxx = gamerxx.lower()
		if gamerxx not in xx:
			print("Було введено невірне значення, спробуйте знову.")
			continue

		computerxx = computerfync(difficulty, gamerxx)
		print(f"Комп'ютер: {computerxx}")
		
		res = winner(gamerxx, computerxx)
		print(res)

		if res == "Ваша перемога!":
			playerwin += 1
		elif res == "Перемога комп'ютера!":
			computerwin += 1

		nowround += 1
		print(f"Раунд {nowround}: Гравець {playerwin} - {computerwin} Комп'ютер")

	if playerwin > computerwin:
		print("Ви перемогли!")
	elif playerwin < computerwin:
		print("Комп'ютер переміг!")
	else:
		print("Нічія!")

	while True:
		againyn = input("Зіграти знову?(y/n): ")

		if againyn.lower() == "y" or againyn.lower() == "n":
			break
		else:
			print("Було введено невірне значення")

	if againyn.lower() == "y" or againyn.lower() == "n":
		if againyn.lower() == "n":
			print("Вихід")
			break

