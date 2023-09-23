import requests
import xml.etree.ElementTree as ET

URL = "https://cbr.ru/scripts/XML_daily.asp" # URL-адрес, по которому будет выполняться HTTP-запрос
response = requests.get(URL) # выполняем HTTP-запрос методом get по указанному URL
# print(response.content)

tree = ET.fromstring(response.text) # Преобразуем строку с XML-данными в объект
print(tree) # выведем объект

code_valute = "USD" # например, доллар
valute_value = None # курс

for valute in tree.findall(".//Valute"):
    char_code = valute.find("CharCode").text
    if char_code == code_valute:
        nominal = valute.find("Nominal").text # например: 10
        name_valute = valute.find("Name").text # например: Египетских фунтов
        valute_value = valute.find("Value").text # 31,53... (рублей)

if valute_value:
    print(f"{nominal} {name_valute} ({code_valute}) = {valute_value} рублей")
else:
    print(f"Курс {code_valute} на текущий день неизвестен")
