vir = input("Введіть вираз через пробіли, наприклад 5 + 5: ")

xx = vir.split()
xx1 = float(xx[0])
op = xx[1]
xx2 = float(xx[2])

if op == "+":
    res = xx1 + xx2
elif op == "-":
    res = xx1 - xx2
elif op == "*":
    res = xx1 * xx2
elif op == "/":
    if xx2 == 0:
        res = "Ділення на нуль"
    else:
        res = xx1 / xx2
else:
    res = "Помилка розпізнавання операції"

print(f"Відповідь: {res}")