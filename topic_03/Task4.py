def sorter(xlist, xword):    
    for xx in range(len(xlist)):
        if xlist[xx] >= xword:
            xpos = xx
            break

    xlist.insert(xpos, xword)

    print(f"Оновленний список: {xlist} \n{xword} було вставлено на позицію {xpos}")

xlist = ['Апельсин', 'Барабан', 'Вечір', 'Закон', 'Яблуко']

while True:
    xword = input('Введіть слово, або "q" щоб вийти: ')

    if xword.lower() == "q":
        print("Вихід")
        break

    xword = xword.capitalize()

    sorter(xlist, xword)