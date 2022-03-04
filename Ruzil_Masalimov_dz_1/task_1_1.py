duration = 400153

second = duration % 60
minute = duration // 60 % 60
hour = duration // 3600 % 24
day = duration // 86400

if day > 0:
    print(f'{day} дн {hour} час {minute} мин {second} сек')
elif hour > 0:
    print(f'{hour} час {minute} мин {second} сек')
elif minute > 0:
    print(f'{minute} мин {second} сек')
else:
    print(f'{second} сек')