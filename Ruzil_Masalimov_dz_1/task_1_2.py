my_list = [i**3 for i in range(1, 1000, 2)]

sum_all = 0

for a in my_list:
    sum_1 = 0
    b = a
    while b != 0:
        sum_1 = sum_1 + b % 10
        b = b // 10
    if sum_1 % 7 == 0:
        sum_all = sum_all + a
print(sum_all)


sum_all_2 = 0
for c in my_list:
    sum_2 = 0
    d = c + 17
    while d != 0:
        sum_2 = sum_2 + d % 10
        d = d // 10
    if sum_2 % 7 == 0:
        sum_all_2 = sum_all_2 + c + 17
print(sum_all_2)
