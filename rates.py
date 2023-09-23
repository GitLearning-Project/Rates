import requests
import xml.etree.ElementTree as ET

URL = "https://cbr.ru/scripts/XML_daily.asp" # URL-адрес, по которому будет выполняться HTTP-запрос
response = requests.get(URL) # выполняем HTTP-запрос методом get по указанному URL
# print(response.content)

tree = ET.fromstring(response.text) # Преобразуем строку с XML-данными в объект
print(tree) # выведем объект

currency_rates = {}  # Словарь для хранения курсов валют

for valute in tree.findall(".//Valute"):
    char_code = valute.find("CharCode").text
    value = valute.find("Value").text
    currency_rates[char_code] = value

# Выводим таблицу с курсами всех валют
print("Курсы валют к рублю:")
print("--------------------")
for char_code, value in currency_rates.items():
    print(f"{char_code}: {value}")
