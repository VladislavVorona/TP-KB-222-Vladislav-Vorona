import requests

def getcourse(xxcode):
	url = f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchangenew?json&valcode={xxcode}"
	resp = requests.get(url)
	
	if resp.status_code == 200:
		base = resp.json()
		if base:
			return base[0]["rate"]
	return None

def getcodes(starting_letter=""):
	url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchangenew?json"
	resp = requests.get(url)
	
	if resp.status_code == 200:
		base = resp.json()
		codes = [entry["cc"] for entry in base if entry["cc"].startswith(starting_letter.upper())]
		return codes
	return []

print("Інформація про найпопулярніші курси валют:")
for code in ["EUR", "USD", "PLN"]:
	rate = getcourse(code)
	print(f"1 {code} = {rate} UAH")


while True:
	xx = input("Введіть перший символ коду валюти (наприклад, E, або 'Q' для виходу): ").upper()
	
	if xx == "Q":
		print("Вихід")
		break

	codes = getcodes(xx)
	
	if not codes:
		print("Немає валют, які починаються з введеного символу.")
		continue
	
	print("Доступні коди валют:")
	for code in codes:
		print(code)
	
	xxcode = input("Введіть код валюти: ").upper()
	
	if xxcode not in codes:
		print("Невірний код валюти. Спробуйте ще раз або введіть 'Q' для виходу.")
		continue

	while True:
		try:
			amount = float(input("Введіть суму для конвертації: "))
			break
		except ValueError:
			print("Було введено невірне значення")
	
	course = getcourse(xxcode)
	
	if course is not None:
		money = amount * course
		print(f"{amount} {xxcode} = {money} UAH")
	else:
		print("Не вдалося отримати курс валюти")
