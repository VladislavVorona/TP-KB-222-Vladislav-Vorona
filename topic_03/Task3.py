xdict = {'R': 'red', 'G': 'green', 'B': 'blue'}

print("\n----------update----------")
print(f"Оригінальний словник: {xdict}")
xdict.update({'Y': "yellow"})
print(f"Відредагований словник: {xdict}")

print("\n----------del----------")
print(f"Оригінальний словник: {xdict}")
del xdict["Y"]
print(f"Відредагований словник: {xdict}")

print("\n----------keys----------")
print(f"Результат: {xdict.keys()}")

print("\n----------values----------")
print(f"Результат: {xdict.values()}")

print("\n----------items----------")
print(f"Результат: {xdict.items()}")

print("\n----------clear----------")
print(f"Оригінальний словник: {xdict}")
xdict.clear()
print(f"Відредагований словник: {xdict}")

print("\n----------Додаткові функції----------")

xdict = {'R': 'red', 'G': 'green', 'B': 'blue'}
print(f"Словник: {xdict}")

print("\n----------get----------")
xdict2 = xdict.get('R') 
print(f"Результат: {xdict2}")

print("\n----------len----------")
xdict2 = len(xdict)
print(f"Результат: {xdict2}")

print("\n----------copy----------")
xdict2 = xdict.copy()
print(f"Результат: {xdict2}")
