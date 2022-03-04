price_list = [57.8, 46.51, 97, 35.5, 49.99, 231.2, 87.7, 652, 99.9, 444, 220.3, 45, 567, 94.5, 377]
new_price = []

for p in price_list:
    r = int(p)
    kk = round((p - r) * 100)
    new_price.append(f'{r} руб {kk:02} коп')
out = (", ".join(new_price))
print(out)

print(id(price_list), price_list)
price_list.sort()
print(id(price_list), price_list)

price_list_min = sorted(price_list, reverse=True)
print(id(price_list_min), price_list_min)

print(price_list[-5:])