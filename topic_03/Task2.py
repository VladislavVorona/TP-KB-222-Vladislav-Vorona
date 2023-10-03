xlist = ['H', 'E', 'L', 'L', 'O']

print("\n----------extend----------")
print(f"Оригінальний список: {xlist}")
xlist.extend(['W', 'O', 'R', 'L', 'D'])
print(f"Відредагований список: {xlist}")

print("\n----------append----------")
print(f"Оригінальний список: {xlist}")
xlist.append('!')
print(f"Відредагований список: {xlist}")

print("\n----------insert----------")
print(f"Оригінальний список: {xlist}")
xlist.insert(5, '_')
print(f"Відредагований список: {xlist}")

print("\n----------remove----------")
print(f"Оригінальний список: {xlist}")
xlist.remove('!')
print(f"Відредагований список: {xlist}")

print("\n----------sort----------")
print(f"Оригінальний список: {xlist}")
xlist.sort()
print(f"Відредагований список: {xlist}")

print("\n----------reverse----------")
print(f"Оригінальний список: {xlist}")
xlist.reverse()
print(f"Відредагований список: {xlist}")

print("\n----------copy----------")
print(f"Оригінальний список: {xlist}")
xlist2 = xlist.copy()
print(f"Скопійований список: {xlist2}")

print("\n----------clear----------")
print(f"Оригінальний список: {xlist2}")
xlist2.clear()
print(f"Відредагований список: {xlist2}")

print("\n----------Додаткові функції----------")

xlist = [1, 2, 5, 1, 4, 5, 7, 5]
print(f"Cписок: {xlist}")

print("\n----------count----------")
xlist2 = xlist.count(5) 
print(f"Результат: {xlist2}")

print("\n----------index----------")
xlist2 = xlist.index(5) 
print(f"Результат: {xlist2}")

print("\n----------len----------")
xlist2 = len(xlist)
print(f"Результат: {xlist2}")

print("\n----------min----------")
xlist2 = min(xlist)
print(f"Результат: {xlist2}")

print("\n----------max----------")
xlist2 = max(xlist)
print(f"Результат: {xlist2}")

print("\n----------sum----------")
xlist2 = sum(xlist)
print(f"Результат: {xlist2}")