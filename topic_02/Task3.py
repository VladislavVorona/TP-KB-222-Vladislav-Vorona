vir = input("Введіть вираз через пробіли, наприклад 5 + 5: ")

xx = vir.split()
xx1 = float(xx[0])
op = xx[1]
xx2 = float(xx[2])


def plus(xx1, xx2):
    return xx1 + xx2

def minus(xx1, xx2):
    return xx1 - xx2

def mno(xx1, xx2):
    return xx1 * xx2

def dil(xx1, xx2):
    if xx2 == 0:
        return "Ділення на нуль"
    else:
        return xx1 / xx2



match op:
    case "+":
        res = plus(xx1, xx2)
    case "-":
        res = minus(xx1, xx2)
    case "*":
        res = mno(xx1, xx2)
    case "/":
        res = dil(xx1, xx2)
    case _:
        res = "Помилка розпізнавання операції."

print(f"Відповідь: {res}")