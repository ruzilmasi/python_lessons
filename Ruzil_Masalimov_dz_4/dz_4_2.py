import requests
from decimal import Decimal


def currency_rates(valute):
    response = requests.get("http://www.cbr.ru/scripts/XML_daily.asp")
    content = response.text
    date = None
    value = None
    name = None
    nominal = None
    for date in content.split('Date='):
        for date_2 in date.split('"')[1:][:1]:
            date = date_2.split('"')[0]
    for el in content.split(f'{valute}'.upper()):
        for el_2 in el.split('<Value>')[1:][:1]:
            value = round(Decimal(el_2.split('</Value>')[0].replace(',', '.')), 2)
        for el_2 in el.split('<Name>')[1:][:1]:
            name = el_2.split('</Name>')[0]
        for el_2 in el.split('<Nominal>')[1:][:1]:
            nominal = el_2.split('</Nominal>')[0]
    return f'Дата: {date}. Курс: 1 рубль = {value} {name}, номинал= {nominal}'



if __name__ == '__main__':
    print(currency_rates('eur'))
    print(currency_rates('USD'))
