vir = input("Введіть вираз через пробіли, наприклад 5 + 5: ")

xx = vir.split()
xx1 = float(xx[0])
op = xx[1]
xx2 = float(xx[2])

match op:
    case "+":
        res = xx1 + xx2
    case "-":
        res = xx1 - xx2
    case "*":
        res = xx1 * xx2
    case "/":
        match xx2:
            case 0:
                res = "Ділення на нуль."
            case _:
                res = xx1 / xx2
    case _:
        res = "Помилка розпізнавання операції."

print(f"Відповідь: {res}")