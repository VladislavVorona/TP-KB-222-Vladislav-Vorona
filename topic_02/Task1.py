import math

a, b, c = -5, 5, 5

def disk(a, b, c):
	disk = b**2 - 4*a*c
	return disk

def roots(a, b, c):
	diskr = disk(a, b, c)
	
	print(f"Дискримінант: {diskr}")

	if diskr > 0:
		xx1 = (-b+math.sqrt(diskr))/(2*a)
		xx2 = (-b-math.sqrt(diskr))/(2*a)
		root = f"x1 = {xx1} та x2 = {xx2}."
		return root

	elif diskr == 0:
		xx1 = -b / (2*a)
		root = f"x = {xx1}"
		return root

	else:
		return f"Отриманий дискримінант ({diskr}) є від'ємним."

print(f"Відповідь: {roots(a, b, c)}")