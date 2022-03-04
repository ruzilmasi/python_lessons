for el in range(1, 101):
    if 15 > el > 10:
        print(f'{el} процентов')
    elif el % 10 == 1:
        print(f'{el} процент')
    elif 5> el % 10 > 1:
        print(f'{el} процента')
    else:
        print(f'{el} процентов')