import requests
import xml.etree.ElementTree as ET

URL = "https://cbr.ru/scripts/XML_daily.asp" # URL-адрес, по которому будет выполняться HTTP-запрос
response = requests.get(URL) # выполняем HTTP-запрос методом get по указанному URL
print(response.content)
