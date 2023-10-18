import random
import numpy as np  # Додано імпорт бібліотеки numpy

# Імпортуємо бібліотеки для роботи з нейронними мережами
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

# Створюємо пусту модель нейронної мережі
model = keras.Sequential([
    layers.Input(shape=(3,)),  # Вхідний шар з 3 нейронів для вибору каменю, ножиць або паперу
    layers.Dense(128, activation='relu'),  # Прихований шар з 128 нейронами та функцією активації ReLU
    layers.Dense(3, activation='softmax')  # Вихідний шар з 3 нейронами та функцією активації softmax
])

# Компілюємо модель з функцією втрати категоріальної характеристики
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Функція для отримання жесту комп'ютера на основі моделі
def computerfync(gamerxx, model):
    xx = ["камінь", "ножиці", "папір"]

    # Отримуємо імовірності вибору для кожного жесту з нейронної мережі
    input_data = [1 if gamerxx == gesture else 0 for gesture in xx]
    input_data = np.array([input_data])  # Використовуємо np.array для створення двовимірного масиву
    probabilities = model.predict(input_data)[0]

    # Вибираємо жест комп'ютера на основі отриманих імовірностей
    computer_choice = random.choices(xx, weights=probabilities)[0]
    return computer_choice

# Функція для навчання моделі під час гри
def train_model(input_data, target):
    input_data = np.array([input_data])  # Перетворюємо вхідні дані у двовимірний масив
    target = np.array([target])  # Перетворюємо ціль у двовимірний масив
    model.train_on_batch(input_data, target)


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
        gamerxx = input("Виберіть ваш жест (камінь, ножиці, папір): ")
        gamerxx = gamerxx.lower()
        if gamerxx not in xx:
            print("Було введено невірне значення, спробуйте знову.")
            continue

        computerxx = computerfync(gamerxx, model)
        print(f"Комп'ютер: {computerxx}")

        res = winner(gamerxx, computerxx)
        print(res)

        if res == "Ваша перемога!":
            playerwin += 1
            # Навчаємо модель на основі гри
            input_data = [1 if gamerxx == gesture else 0 for gesture in xx]
            target = [1 if computerxx == gesture else 0 for gesture in xx]
            train_model(input_data, target)
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
        againyn = input("Зіграти знову? (y/n): ")

        if againyn.lower() == "y" or againyn.lower() == "n":
            break
        else:
            print("Було введено невірне значення")

    if againyn.lower() == "n":
        print("Вихід")
        break
