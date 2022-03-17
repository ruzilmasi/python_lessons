def thesaurus(*args):
    dict = {}
    for name in args:
        key = name[0]
        if key not in dict:
            dict[key] = []
        dict[key].append(name)
    print(dict)

thesaurus("Иван", "Мария", "Петр", "Илья")