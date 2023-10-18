from functions import *
from operations import getxx

while True:
    xx1, op, xx2 = getxx()

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
