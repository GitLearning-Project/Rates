import requests
import xml.etree.ElementTree as ET

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
        print(f"{currency_data['nominal']}  {currency_data['name']}     ({code_valute}) = {currency_data['value']} рублей")
    else:
        print(f"Курс {code_valute} на текущий день неизвестен")


URL = "https://cbr.ru/scripts/XML_daily.asp"
currency_tree = get_currency_data(URL)

user_case = int(input("Вывести информацию по коду валюты - введите 1\nВывести таблицу курсов всех валют к рублю - введите 2\n"))

if user_case == 1:
    # Вывод курса определённой валюты
    code_valute = input("Введите код валюты: ").upper()
    currency_data =     get_currency_by_code(currency_tree, code_valute)
    display_currency_info(currency_data)
else:
    # Вывод курсов всех валют по отношению к рублю
    currency_rates = {}

    for valute in currency_tree.findall(".//    Valute"):
        char_code = valute.find("CharCode").text
        value = valute.find("Value").text
        currency_rates[char_code] = value

    print("Курсы валют к рублю:")
    print("------------------")
    for char_code, value in currency_rates.items():
        print(f"{char_code}: {value}")
