import requests
import xml.etree.ElementTree as ET
import datetime

def get_currency_data(url):
    response = requests.get(url)
    tree = ET.fromstring(response.text)
    return tree

def get_currency_by_code(currency_tree, code):
    for valute in currency_tree.findall(".//Valute"):
        char_code = valute.find("CharCode").text
        if char_code == code:
            nominal = valute.find("Nominal").text
            name_valute = valute.find("Name").text
            valute_value = valute.find("Value").text
            return {
                "nominal": nominal,
                "name": name_valute,
                "value": valute_value
            }
    return None

def display_currency_info(currency_data):
    if currency_data:
        print(f"{currency_data['nominal']} {currency_data['name']} ({code_valute}) = {currency_data['value']} рублей")
    else:
        print(f"Курс {code_valute} на текущий день неизвестен")

def save_currency_exchange_rates(currency_rates):
    with open("exchange_rates.txt", "a", encoding="utf-8") as file:
        current_datetime = datetime.datetime.now()
        file.write(f"Дата и время сохранения: {current_datetime}\n")
        for char_code, value in currency_rates.items():
            file.write(f"{char_code}: {value}\n")
        file.write("--------------------------\n")

def display_all_currency_rates(currency_tree):
    currency_rates = {}

    for valute in currency_tree.findall(".//Valute"):
        char_code = valute.find("CharCode").text
        value = valute.find("Value").text
        currency_rates[char_code] = value

    print("Курсы валют к рублю:")
    print("--------------------")
    for char_code, value in currency_rates.items():
        print(f"{char_code}: {value}")
    # Сохраняем список курсов в файл exchange_rates.txt
    save_currency_exchange_rates(currency_rates)


URL = "https://cbr.ru/scripts/XML_daily.asp"
currency_tree = get_currency_data(URL)

user_case = int(input("Вывести информацию по коду валюты - введите 1\nВывести таблицу курсов всех валют к рублю - введите 2\n"))

if user_case == 1:
    code_valute = input("Введите код валюты: ").upper()
    currency_data = get_currency_by_code(currency_tree, code_valute)
    display_currency_info(currency_data)
else:
    display_all_currency_rates(currency_tree)
