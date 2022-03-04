my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

new_list = []
for el in my_list:
    name = (el.split()[-1]).capitalize()
    for hello in name:
        hello = f'Привет, {name}!'
    new_list.extend([hello])

for i in new_list:
    print(i)