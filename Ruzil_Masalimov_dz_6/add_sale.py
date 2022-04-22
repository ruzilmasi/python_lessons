import sys


def add_sale(sale):
    with open('bakery.csv', 'a', encoding='utf-8') as f:
        print(f'{sale}', file=f)

print(add_sale(sys.argv[1:][0]))
