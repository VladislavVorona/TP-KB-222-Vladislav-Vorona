xx = input("Введіть завдання для знаходження дискримінанту, використовуючи пробіли між числами, наприклад -2 +4 -1: ")

a, b, c = map(float, xx.split())

def disk(a, b, c):
    disk = b**2 - 4*a*c
    return disk


print(f"Відповідь: {disk(a, b, c)}")