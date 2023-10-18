import random
import numpy as np
import os
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

if not os.path.exists("TPModels"):
	os.mkdir("Topic5.keras")

if os.path.exists(os.path.join("TPModels", "Topic5.keras")):
	model = keras.models.load_model(os.path.join("TPModels", "Topic5.keras"))
else:
	model = keras.Sequential([
		layers.Input(shape=(3,)),
		layers.Dense(128, activation='relu'),
		layers.Dense(3, activation='softmax')
	])
	model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

def computerfync(gamerxx, model):
	xx = ["камінь", "ножиці", "папір"]

	gamerdata = [1 if gamerxx == gesture else 0 for gesture in xx]
	gamerdata = np.array([gamerdata])
	probabilities = model.predict(gamerdata)[0]

	computer_choice = random.choices(xx, weights=probabilities)[0]
	return computer_choice

def train(gamerdata, target):
	gamerdata = np.array([gamerdata])
	target = np.array([target])
	model.train_on_batch(gamerdata, target)


def winner(gamerxx, computerxx):
	if gamerxx == computerxx:
		return "Нічія!"
	elif (gamerxx == "камінь" and computerxx == "ножиці") or (gamerxx == "ножиці" and computerxx == "папір") or (gamerxx == "папір" and computerxx == "камінь"):
		return "Ваша перемога!"
	else:
		return "Перемога комп'ютера!"


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

	nowround = 0

	while nowround < rounds:
		xx = ["камінь", "ножиці", "папір"]
		gamerxx = random.choice(xx)

		computerxx = computerfync(gamerxx, model)
		print(f"Комп'ютер: {computerxx}")

		res = winner(gamerxx, computerxx)
		print(res)

		if res == "Ваша перемога!":
			playerwin += 1

		elif res == "Перемога комп'ютера!":
			computerwin += 1
			gamerdata = [1 if gamerxx == gesture else 0 for gesture in xx]
			target = [1 if computerxx == gesture else 0 for gesture in xx]
			train(gamerdata, target)


		nowround += 1
		print(f"Раунд {nowround}: Гравець {playerwin} - {computerwin} Комп'ютер")

	if playerwin > computerwin:
		print("Ви перемогли!")
	elif playerwin < computerwin:
		print("Комп'ютер переміг!")
	else:
		print("Нічія!")

	while True:
		model.save(os.path.join("TPModels", "Topic5.keras"))
		againyn = input("Зіграти знову? (y/n): ")

		if againyn.lower() == "y" or againyn.lower() == "n":
			break
		else:
			print("Було введено невірне значення")

	if againyn.lower() == "n":
		print("Вихід")
		break
