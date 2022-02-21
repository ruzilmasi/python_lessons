for el in range(1, 101):
    if el % 10 == 1:
        print(f'{el} процент')
    elif 5> el % 10 > 1:
        print(f'{el} процента')
    else:
        print(f'{el} процентов')