print("----------strip----------")

text = input("Текст для функції strip: ")
print(f"\nОрігінальний текст: {text}\nВідредагований текст: {text.strip()}")

print("----------capitalize----------")

text = input("Текст для функції capitalize: ")
print(f"\nОрігінальний текст: {text}\nВідредагований текст: {text.capitalize()}")

print("----------title----------")

text = input("Текст для функції title: ")
print(f"\nОрігінальний текст: {text}\nВідредагований текст: {text.title()}")

print("----------upper----------")

text = input("Текст для функції upper: ")
print(f"\nОрігінальний текст: {text}\nВідредагований текст: {text.upper()}")

print("----------lower----------")

text = input("Текст для функції lower: ")
print(f"\nОрігінальний текст: {text}\nВідредагований текст: {text.lower()}")

print("----------swapcase----------")

text = input("Текст для функції swapcase: ")
print(f"\nОрігінальний текст: {text}\nВідредагований текст: {text.swapcase()}")

print("----------replace----------")

text = input("Текст для функції replace: ")
repl = input("Введіть текст для заміни через ;. Наприклад, якщо вам потрібно замінити слово Привіт на Вітаю, то потрібно написати: Привіт;Вітаю. : ")
repl = repl.split(";")
print(f"\nОрігінальний текст: {text}\nВідредагований текст: {text.replace(repl[0], repl[1])}")